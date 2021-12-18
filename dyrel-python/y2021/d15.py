from re import S
from common import getPuzzle, submitSecure
from collections import deque, Counter
from functools import reduce
from operator import mul
from itertools import permutations, takewhile, accumulate, count, islice
import heapq as pq

NEIGHBOUR4 = ((1, 0), (0, 1), (-1, 0), (0, -1))

puzzle = getPuzzle()

rawInput = puzzle.input_data
# rawInput = """1163751742
# 1381373672
# 2136511328
# 3694931569
# 7463417111
# 1319128137
# 1359912421
# 3125421639
# 1293138521
# 2311944581"""

def parseInput1(inp):
    d = dict()
    w, h = 0, 0
    for ri, r in enumerate(inp.splitlines()):
        h = max(ri, h)
        for ci, c in enumerate(r):
            d[(ri, ci)] = int(c)
            w = max(ci, w)
    return d, w + 1, h + 1

def parseInput2(inp):
    d0, w0, h0 = parseInput1(inp)
    d = dict()
    for p0, v0 in d0.items():
        for dr in range(5):
            for dc in range(5):
                r0, c0 = p0
                r, c = dr*h0 + r0, dc*w0 + c0
                v = (dr + dc + v0 - 1) % 9 + 1
                d[(r, c)] = v
    return d, w0*5, h0*5

def findTotalRisk(risk, width, height):
    totRisk = dict()
    totRisk[(0, 0)] = 0
    prioQueue = [(0, 0, 0)]
    lastPos = (height - 1, width - 1)
    while len(prioQueue) > 0:
        _, r0, c0 = pq.heappop(prioQueue)
        v0 = totRisk[(r0, c0)]
        for dr, dc in NEIGHBOUR4:
            p = (r0+dr, c0+dc)
            if p not in risk:
                continue
            v = v0 + risk[p]
            if p not in totRisk or v < totRisk[p]:
                totRisk[p] = v
                pq.heappush(prioQueue, (v, r0+dr, c0+dc))
        if lastPos in totRisk:
            return totRisk[lastPos]

risk, width, height = parseInput1(rawInput)
print(findTotalRisk(risk, width, height))
risk, width, height = parseInput2(rawInput)
print(findTotalRisk(risk, width, height))