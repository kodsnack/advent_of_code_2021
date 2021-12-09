from common import getPuzzle, submitSecure
from collections import deque
from functools import reduce
from operator import mul

puzzle = getPuzzle()

rawInput = puzzle.input_data

def parseInput(inp):
    d = dict()
    for ridx, row in enumerate(inp.splitlines()):
        for cidx, col in enumerate(row):
            d[cidx+1j*ridx] = int(col)
    return d

inp = parseInput(rawInput)
sm = sum((v+1) for k, v in inp.items()
               if v < min(inp.get(c+k, 10) for c in (1, -1, 1j, -1j)))
submitSecure(puzzle, "a", sm)

def findBasins(heightMap):
    processed = set()
    basins = list()
    q = deque()
    for pos, height in heightMap.items():
        if pos in processed or height == 9:
            continue
        newBasin = set()
        q.append(pos)
        while len(q) > 0:
            newPosition = q.popleft()
            if newPosition in processed:
                continue
            newHeight = heightMap.get(newPosition, 9)
            if newHeight == 9:
                continue
            newBasin.add(newPosition)
            processed.add(newPosition)
            q.extend(newPosition + delta
                     for  delta in (1, -1, 1j, -1j))
        basins.append(newBasin)
    return basins

basins = findBasins(inp)
basinSizes = sorted(list(map(len, basins)))
submitSecure(puzzle, "b", reduce(mul, basinSizes[-3:]))
