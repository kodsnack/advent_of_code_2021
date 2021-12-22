from common import getPuzzle, submitSecure
from collections import Counter

NEIGHBOUR4 = (-1, -1j, 1, +1j)
NEIGHBOUR5 = (-1, -1j, 1, +1j, 0)
NEIGHBOUR8 = (-1-1j, -1j, 1-1j, -1, 1, -1+1j, 1j, 1+1j)
NEIGHBOUR9 = (-1-1j, -1j, 1-1j, -1, 0, 1, -1+1j, 1j, 1+1j)

puzzle = getPuzzle()

rawInput = puzzle.input_data

def parseInput(inp):
    return tuple(map(lambda x:int(x.split()[4]), inp.splitlines()))

startPos1, startPos2 = parseInput(rawInput)

def move(pos, diceVal):
    return (pos - 1 + diceVal) % 10 + 1

def d100():
    die = 1
    while True:
        yield die
        die = die % 100 + 1

def moveDice(p, die):
    ds = 0
    for i in range(3):
        ds += next(die)
    p = ((p - 1) + ds) % 10 + 1
    return p, die

inp = parseInput(rawInput)
p1, p2 = startPos1, startPos2
die = d100()
ps1, ps2 = 0, 0
nor = 0
while True:
    p1, die = moveDice(p1, die)
    nor += 3
    ps1 += p1
    if ps1 >= 1000:
        break
    p2, die = moveDice(p2, die)
    nor += 3
    ps2 += p2
    if ps2 >= 1000:
        break
if ps1 >= 1000:
    ans = ps2*nor
else:
    ans = ps1*nor

submitSecure(puzzle, "a", ans)

d3Outcomes = dict()
for d1 in range(1, 4):
    for d2 in range(1, 4):
        for d3 in range(1, 4):
            d3Outcomes[d1+d2+d3] = d3Outcomes.get(d1+d2+d3,0)+1


def rollQuantumDice(uni, pi):
    newUni = Counter()
    for state, n in uni.items():
        if state[2] >= 21 or state[3] >= 21:
            newUni[state] += n
            continue
        for diceResult, outcomes in d3Outcomes.items():
            playerPos = state[pi] + diceResult
            if playerPos > 10:
                playerPos -= 10
            newPs = state[2+pi] + playerPos
            if pi == 0:
                newUni[(playerPos, state[1], newPs, state[3])] += n*outcomes
            else:
                newUni[(state[0], playerPos, state[2], newPs)] += n*outcomes
    return newUni

def allFinished(uni):
    return all(map(lambda x:x[2]>20 or x[3]>20, uni))

def wonStates(states, player):
    return sum((v for k, v in states.items() if k[2+player] > 20))

states = {(startPos1, startPos2, 0, 0):1}
playerTurn = 0
while True:
    states = rollQuantumDice(states, playerTurn)
    finished = allFinished(states)
    if finished:
        break
    playerTurn = 1 - playerTurn

submitSecure(puzzle, "b", wonStates(states, playerTurn))
