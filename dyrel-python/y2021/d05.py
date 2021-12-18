from common import getPuzzle, submitSecure
from collections import Counter

puzzle = getPuzzle()

rawInput = puzzle.input_data
def parseInput(inp):
    l = list()
    for line in inp.splitlines():
        p1, _, p2 = line.split()
        x1, y1, x2, y2 = int(p1.split(",")[0]), int(p1.split(",")[1]), int(p2.split(",")[0]), int(p2.split(",")[1])
        l.append((x1, y1, x2, y2))
    return l

def sign(i):
    return i/abs(i)

def absrange(i1, i2, offset=0):
    return range(offset, offset + max(i1, i2) - min(i1, i2) + 1)

inp = parseInput(rawInput)
ventMap1 = Counter()
ventMap2 = Counter()
for x1, y1, x2, y2 in inp:
    if x1!=x2 and y1!=y2:
        deltax, deltay = sign(x2-x1), sign(y2-y1)
        ventMap2.update((x1 + deltax*i, y1 + deltay*i) for i in absrange(x1, x2))
    else:
        ventMap1.update((x, y)
                        for x in absrange(x1, x2, min(x1, x2))
                        for y in absrange(y1, y2, min(y1, y2)))
submitSecure(puzzle, "a", sum(v>1 for v in ventMap1.values()))
ventMap2.update(ventMap1)
submitSecure(puzzle, "b", sum(v>1 for v in ventMap2.values()))
