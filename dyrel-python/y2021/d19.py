from re import S
from common import getPuzzle, submitSecure
from collections import deque, Counter
from functools import reduce
from operator import mul
from itertools import permutations, takewhile, accumulate, count, islice, chain

NEIGHBOUR4 = (-1, -1j, 1, +1j)
NEIGHBOUR5 = (-1, -1j, 1, +1j, 0)
NEIGHBOUR8 = (-1-1j, -1j, 1-1j, -1, 1, -1+1j, 1j, 1+1j)
NEIGHBOUR9 = (-1-1j, -1j, 1-1j, -1, 0, 1, -1+1j, 1j, 1+1j)

puzzle = getPuzzle()

rawInput = puzzle.input_data

def parseInput(inp):
    d = dict()
    nr = 0
    for line in inp.splitlines():
        if len(line) == 0:
            continue
        if line[1] == '-':
            _, _, nr, _ = line.split()
            nr = int(nr)
            d[nr] = list()
        else:
            a, b, c = line.split(',')
            d[nr].append((int(a), int(b), int(c)))
    return d

def mmul(a, b):
    l = list()
    for row in range(3):
        l.append([])
        for col in range(3):
            s = 0
            for item in range(3):
                s += a[row][item]*b[item][col]
            l[-1].append(s)
    return (tuple(l[0]), tuple(l[1]), tuple(l[2]))

def rx(p):
    return p[0], -p[2], p[1]

def r2x(p):
    return p[0], -p[1], -p[2]

def r3x(p):
    return p[0], p[2], -p[1]

def ry(p):
    return -p[2], p[1], p[0]

def r2y(p):
    return -p[0], p[1], -p[2]

def r3y(p):
    return p[2], p[1], -p[0]

def rz(p):
    return -p[1], p[0], p[2]

def r2z(p):
    return -p[0], -p[1], p[2]

def r3z(p):
    return p[1], -p[0], p[2]

def ri(p):
    return p[0], p[1], p[2]

rotf = (ri, rx, r2x, r3x,
        lambda p:ry(ri(p)), lambda p:ry(rx(p)), lambda p:ry(r2x(p)), lambda p:ry(r3x(p)),
        lambda p:r3y(ri(p)), lambda p:r3y(rx(p)), lambda p:r3y(r2x(p)), lambda p:r3y(r3x(p)),
        lambda p:rz(ri(p)), lambda p:rz(rx(p)), lambda p:rz(r2x(p)), lambda p:rz(r3x(p)),
        lambda p:r3z(ri(p)), lambda p:r3z(rx(p)), lambda p:r3z(r2x(p)), lambda p:r3z(r3x(p)),
        lambda p:r2y(ri(p)), lambda p:r2y(rx(p)), lambda p:r2y(r2x(p)), lambda p:r2y(r3x(p)),
        )

s= set()
b = (1, 2, 3)
for rf in rotf:
    s.add(rf(b))
print(s)
assert len(s) == 24

def rotations():
    rz = ((0, -1, 0), (1, 0, 0), (0, 0, 1))
    rx = ((1, 0, 0), (0, 0, -1), (0, 1, 0))
    ry = ((0, 0, 1), (0, 1, 0), (-1, 0, 0))
    base = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    s = set()
    s.add(base)
    while True:
        s2 = set()
        for i in s:
            s2.add(i)
            s2.add(mmul(i, rx))
            s2.add(mmul(i, ry))
            s2.add(mmul(i, rz))
        if len(s2) == len(s):
            return s2
        s = s2

def vmul(m, v):
    x = v[0]*m[0][0] + v[1]*m[0][1] + v[2]*m[0][2]
    y = v[0]*m[1][0] + v[1]*m[1][1] + v[2]*m[1][2]
    z = v[0]*m[2][0] + v[1]*m[2][1] + v[2]*m[2][2]
    return (x, y, z)

def vsmul(m, vs):
    return set((vmul(m, v) for v in vs))

def vminus(a, b):
    return (a[0]-b[0], a[1]-b[1], a[2]-b[2])

def vsminus(a_s, b):
    return set((vminus(a, b) for a in a_s))

def measure(scanner):
    xs = [x for x, _, _ in scanner]
    xmeas = Counter((abs(x1-x2)) for x1 in xs for x2 in xs)
    return xmeas

def fit(scan, comp):
    for rotScan in scan:
        for refPoint in comp:
            for scannerPoint in rotScan:
                delta = vminus(scannerPoint, refPoint)
                translated = set((vminus(point, delta) for point in rotScan))
                hits = len(translated & comp)
                if hits > 11:
                    return (hits, delta, translated)
    return (0, 0, 0)

def applyAllRotations(rots, scannerList):
    newScannerList = dict()
    for nr, scanners in scannerList.items():
        l = list()
        for rot in rots:
            l.append(vsmul(rot, scanners))
        newScannerList[nr] = l
    return newScannerList

allRots = rotations()
assert len(allRots)==24

def findScanner(scanners, foundSoFar, triedCombintations, scannerPoss):
    notFoundScanners = dict()
    foundScanners = dict(foundSoFar)
    for scanner in scanners:
        for found in foundSoFar:
            print("Testing ", scanner, "vs", found)
            if (scanner, found) in triedCombintations:
                continue
            triedCombintations.add((scanner, found))
            hits, pos, newPoss = fit(scanners[scanner],
                                     foundSoFar[found])
            if hits > 11:
                print(scanner, "matched", found)
                foundScanners[scanner] = newPoss
                scannerPoss.append(pos)
                break
        if scanner not in foundScanners:
            notFoundScanners[scanner] = scanners[scanner]
    return notFoundScanners, foundScanners, triedCombintations, scannerPoss

inp = parseInput(rawInput)
found = dict()
found[0] = set(inp[0])
scannerPos = list()
triedCombinations = set()
del inp[0]
inp = applyAllRotations(allRots, inp)
print(len(inp), len(found))
while len(inp) > 0:
    inp, found, triedCombinations, scannerPos = findScanner(inp, found, triedCombinations, scannerPos)
    print(len(inp), len(found))


s = reduce(set.union, found.values())
submitSecure(puzzle, "a", len(s))

def manhDist(p1, p2):
    return sum(map(lambda x, y:abs(x-y), p1, p2))

submitSecure(puzzle, "b", max((manhDist(x, y) for x in scannerPos
                                              for y in scannerPos)))
