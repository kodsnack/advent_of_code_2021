from functools import reduce
from common import getPuzzle

puzzle = getPuzzle()

rawInput = puzzle.input_data

def partAbs(z: complex):
    return abs(z.real) + 1j*abs(z.imag)

def foldFunc(fold: complex):
    return lambda x: partAbs(fold - partAbs(x - fold))

def chainFunc(first, second):
    return lambda x: second(first(x))

def parseFold(line: str):
    _, _, c = line.split()
    return {"x":1, "y":1j}[c[0]] * int(c[2:])

def parseDot(line: str):
    x, y = line.split(',')
    return int(x) + int(y)*1j

def parseInput(inp: str):
    dotInp, foldInp = inp.split("\n\n")
    return ([parseDot(line) for line in dotInp.splitlines()],
            [parseFold(line) for line in foldInp.splitlines()])

def partAbs(z: complex):
    return abs(z.real) + 1j*abs(z.imag)

def drawDots(dots: set):
    return '\n'.join((''.join(("X" if x+1j*y in dots else " ")
                      for x in range(int(min(x.real for x in dots)), 
                                     int(max(x.real for x in dots))+1)))
                     for y in range(int(min(y.imag for y in dots)),
                                    int(max(y.imag for y in dots))+1))

dots, folds = parseInput(rawInput)

f1 = foldFunc(folds[0])
fn = reduce(chainFunc, (foldFunc(fold) for fold in folds))

print(len(set((f1(dot) for dot in dots))))
print(drawDots(set((fn(dot) for dot in dots))))
