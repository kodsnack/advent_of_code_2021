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

def parseInput(inp):
    words = inp.split()
    xvals = words[2][2:-1]
    yvals = words[3][2:]
    xmin = int(xvals.split('..')[0])
    xmax = int(xvals.split('..')[1])
    xmin = int(yvals.split('..')[0])
    xmin = int(yvals.split('..')[1])
    return (xmin, xmax, ymin, ymax)

def simulate(vx, vy, xmin, xmax, ymin, ymax):
    x, y = 0, 0
    yy = 0
    while x < xmax and y > ymin:
        x += vx
        y += vy
        if vx < 0:
            vx += 1
        if vx > 0:
            vx -= 1
        vy -= 1
        yy = max(y, yy)
        if xmin <= x <= xmax and ymin <= y <= ymax:
            return yy
    return None

xmin, xmax, ymin, ymax = parseInput(rawInput)

y = 0
count = 0
for vx in range(xmax+1):
    for vy in range(ymin, -ymin+1):
        yy = simulate(vx, vy, xmin, xmax, ymin, ymax)
        if yy != None:
            y = max(y, yy)
            count += 1

submitSecure(puzzle, "a", y)
submitSecure(puzzle, "b", count)
