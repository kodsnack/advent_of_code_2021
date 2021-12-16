from common import getPuzzle
from functools import reduce
from operator import mul

puzzle = getPuzzle()

rawInput = puzzle.input_data

def parseInput(inp):
    l = list()
    for c in inp:
        l.append(bin(int(c, 16)+16)[3:])
    return ''.join(l)

def readBits(inp, pos, bits):
    v = int(inp[pos:pos+bits], 2)
    return v, pos+bits

def readPacket(inp, pos):
    v, pos = readBits(inp, pos, 3)
    t, pos = readBits(inp, pos, 3)
    if t == 4:
        tot = 0
        while True:
            b, pos = readBits(inp, pos, 5)
            tot = tot*16 + (b % 16)
            if b < 16:
                break
        return pos, [v, t, tot]
    else:
        children = []
        ltid, pos = readBits(inp, pos, 1)
        if ltid == 0:
            tlib, pos = readBits(inp, pos, 15)
            targetPos = pos + tlib
            while pos < targetPos:
                pos, vv = readPacket(inp, pos)
                children.append(vv)
        else:
            nsp, pos = readBits(inp, pos, 11)
            for i in range(nsp):
                pos, vv = readPacket(inp, pos)
                children.append(vv)
        return pos, [v, t, children]

def sumVersions(packetTree):
    v, t, payload = packetTree
    if t == 4:
        return v
    else:
        return v + sum(map(sumVersions, payload))

def totalValue(packetTree):
    _, t, payload = packetTree
    if t == 4:
        return payload
    else:
        values = list(map(totalValue, payload))
        if t == 0:
            return sum(values)
        elif t == 1:
            return reduce(mul, values)
        elif t == 2:
            return min(values)
        elif t == 3:
            return max(values)
        elif t == 5:
            return int(values[0] > values[1])
        elif t == 6:
            return int(values[0] < values[1])
        elif t == 7:
            return int(values[0] == values[1])
    assert False

inp = parseInput(rawInput)
_, tree = readPacket(inp, 0)
print(sumVersions(tree))
print(totalValue(tree))
