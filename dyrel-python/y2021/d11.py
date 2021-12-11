from re import S
from common import getPuzzle, submitSecure
from collections import deque, Counter
from functools import reduce
from operator import mul
from itertools import permutations, takewhile, accumulate, count, islice

NEIGHBOUR4 = (-1, -1j, 1, +1j)
NEIGHBOUR5 = (-1, -1j, 1, +1j, 0)
NEIGHBOUR8 = (-1-1j, -1j, 1-1j, -1, 1, -1+1j, 1j, 1+1j)
NEIGHBOUR9 = (-1-1j, -1j, 1-1j, -1, 0, 1, -1+1j, 1j, 1+1j)

puzzle = getPuzzle()

rawInput = puzzle.input_data
# rawInput = """5483143223
# 2745854711
# 5264556173
# 6141336146
# 6357385478
# 4167524645
# 2176841721
# 6882881134
# 4846848554
# 5283751526"""
def parseInput(inp):
    d = dict()
    for ri, r in enumerate(inp.splitlines()):
        for ci, c in enumerate(r):
            d[ci+1j*ri] = int(c)
    return d

def stepSquids(squids):
    hasFlashed = set()
    for sq_pos in squids:
        squids[sq_pos] += 1
    flashing = deque(sq_pos for sq_pos in squids if squids[sq_pos] > 9)
    while len(flashing) > 0:
        sq_pos = flashing.pop()
        if sq_pos in hasFlashed:
            continue
        for delta in NEIGHBOUR8:
            new_pos = sq_pos + delta
            if new_pos not in squids:
                continue
            squids[new_pos] += 1
            if squids[new_pos] > 9:
                flashing.append(new_pos)
        hasFlashed.add(sq_pos)
    for sq_pos in hasFlashed:
        squids[sq_pos] = 0
    return len(hasFlashed)

def squidStepper(squids):
    while True:
        yield stepSquids(squids)

squids = parseInput(rawInput)
submitSecure(puzzle, "a", sum(islice(squidStepper(squids), 100)))

squids = parseInput(rawInput)
submitSecure(puzzle, "b", 
             len(tuple(takewhile(lambda x: x<100, squidStepper(squids))))+1)
