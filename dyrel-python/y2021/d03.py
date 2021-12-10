from common import getPuzzle, submitSecure

puzzle = getPuzzle()

def findMostBit(inp, bit):
    l = [line[bit] for line in inp]
    if l.count("0") > l.count("1"):
        return "0"
    else:
        return "1"

def findLeastBit(inp, bit):
    return {"1":"0", "0":"1"}[findMostBit(inp, bit)]

def filterBit(inp, pos, val):
    l = list()
    for line in inp:
        if line[pos] == val:
            l.append(line)
    if len(l)>0:
        return l
    return inp[-1]

inp = list(puzzle.input_data.splitlines())
g = ''.join([findLeastBit(inp, pos) for pos in range(len(inp[0]))])
e = ''.join([findMostBit(inp, pos) for pos in range(len(inp[0]))])
print(f"gamma={g}, epsilon={e}")
submitSecure(puzzle, "a", int(g,2)*int(e,2))

oxy, co2 = list(inp), list(inp)
pos = 0
while len(oxy)>1 and len(co2)>1:
    bm = findMostBit(oxy, pos)
    bl = findLeastBit(co2, pos)
    oxy = filterBit(oxy, pos, bm)
    co2 = filterBit(co2, pos, bl)
    pos += 1
print(f"oxygen={oxy[0]}, co2={co2[0]}")
submitSecure(puzzle, "b", int(oxy[0], 2)*int(co2[0], 2))
