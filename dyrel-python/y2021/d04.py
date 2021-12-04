from common import getPuzzle, submitSecure

puzzle = getPuzzle()

def parseInput(inp):
    l = list(inp.splitlines())
    n = list(map(int, l[0].split(',')))
    bl = list()
    for i in range(2, len(l), 6):
        b = [set() for i in range(10)]
        for lno, line in enumerate(l[i:i+5]):
            for cno, item in enumerate(line.split()):
                b[lno].add(int(item))
                b[cno+5].add(int(item))
        bl.append(b)
    return n, bl

def won(nums, brd):
    for s in brd[:-1]:
        if len(s-nums) == 0:
            return True
    return False

def calcScore(board, drawnNumbers, lastNumber):
    return sum(set(i for bs in board for i in bs) - drawnNumbers) * lastNumber

numbers, boards = parseInput(puzzle.input_data)
alreadyWon = set()
winningScores = list()
drawnNumbers = set()
for number in numbers:
    drawnNumbers.add(number)
    for boardIdx, board in enumerate(boards):
        if boardIdx in alreadyWon:
            continue 
        if won(drawnNumbers, board):
            winningScores.append(calcScore(board, drawnNumbers, number))
            alreadyWon.add(boardIdx)
submitSecure(puzzle, "a", winningScores[0])
submitSecure(puzzle, "b", winningScores[-1])
