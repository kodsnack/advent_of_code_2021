from common import getPuzzle, submitSecure
from collections import deque
from functools import reduce

puzzle = getPuzzle()
rawInput = puzzle.input_data


def parseNumber(line):
    d = deque()
    for c in line:
        if c.isdigit():
            d[-1].append(int(c))
        elif c == '[':
            d.append(list())
        elif c == ']':
            pair = d.pop()
            if len(d) > 0:
                d[-1].append(pair)
            else:
                return pair
        elif c == ",":
            pass
        else:
            assert False, "unexpected"


def parseInput(inp):
    l = list()
    for line in inp.splitlines():
        l.append(parseNumber(line))
    return l


def isPurePair(p):
    return (not isinstance(p[0], list)) and (not isinstance(p[1], list))


def addRight(p, r):
    if not isinstance(p, list):
        return p+r, 0
    leftTree, remain = addRight(p[0], r)
    if remain == 0:
        return [leftTree, p[1]], 0
    rightTree, remain = addRight(p[1], remain)
    return [leftTree, rightTree], remain


def addLeft(p, l):
    if not isinstance(p, list):
        return p+l, 0
    rightTree, remain = addLeft(p[1], l)
    if remain == 0:
        return [p[0], rightTree], 0
    leftTree, addRight = addLeft(p[0], remain)
    return [leftTree, rightTree], remain


def doExplode(p, depth=0):
    if not isinstance(p, list):
        return False, 0, p, 0
    if depth >= 4 and isPurePair(p):
        return True, p[0], 0, p[1]
    changed, leftAdd, middle, rightAdd = doExplode(p[0], depth+1)
    if changed:
        right, rightAdd = addRight(p[1], rightAdd)
        return changed, leftAdd, [middle, right], rightAdd
    changed, leftAdd, middle, rightAdd = doExplode(p[1], depth+1)
    if changed:
        left, leftAdd = addLeft(p[0], leftAdd)
        return changed, leftAdd, [left, middle], rightAdd
    return False, 0, p, 0


def doSplit(p):
    if isinstance(p, list):
        changed, leftP = doSplit(p[0])
        if changed:
            return changed, [leftP, p[1]]
        changed, rightP = doSplit(p[1])
        if changed:
            return changed, [leftP, rightP]
        return False, p
    elif p >= 10:
        return True, [p//2, (p+1)//2]
    else:
        return False, p


def reducePair(p):
    while True:
        changed, _, newP, _ = doExplode(p)
        if changed:
            p = newP
            continue
        changed, newP = doSplit(p)
        if changed:
            p = newP
            continue
        break
    return p


def addPair(p1, p2):
    return reducePair([p1, p2])


def calcMagnitude(p):
    if isinstance(p, list):
        return 3*calcMagnitude(p[0]) + 2*calcMagnitude(p[1])
    return p


inp = parseInput(rawInput)

submitSecure(puzzle, "a", calcMagnitude(reduce(addPair, inp)))

submitSecure(puzzle, "b", max((max(calcMagnitude(addPair(x, y)), 
                                   calcMagnitude(addPair(y, x)))
                               for x in inp for y in inp)))
