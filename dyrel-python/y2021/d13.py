from common import getPuzzle, submitSecure

puzzle = getPuzzle()

rawInput = puzzle.input_data

def parseInput(inp):
    dots = set()
    folds = list()
    for line in inp.splitlines():
        if line[:4]=="fold":
            a, b, c = line.split()
            folds.append((c[0], int(c[2:])))
        elif line!="":
            x, y = line.split(",")
            dots.add((int(x), int(y)))
    return dots, folds

def doFold(dots, axis, line):
    result = set()
    for dot in dots:
        x, y = dot
        if axis == 'x':
            if x > line:
                x = line - (x - line)
            result.add((x, y))
        if axis == 'y':
            if y > line:
                y = line - (y - line)
            result.add((x, y))
    return result

def printDots(dots):
    minx, maxx = min(x for x, y in dots), max(x for x, y in dots)
    miny, maxy = min(y for x, y in dots), max(y for x, y in dots)
    for y in range(miny, maxy+1):
        for x in range(minx, maxx+1):
            if (x, y) in dots:
                print("X", end="")
            else:
                print(" ", end="")
        print()


dots, folds = parseInput(rawInput)

for fold in folds[:1]:
    axis, line = fold
    dots = doFold(dots, axis, line)
submitSecure(puzzle, "a", len(dots))

for fold in folds[1:]:
    axis, line = fold
    dots = doFold(dots, axis, line)

printDots(dots)
# submitSecure(puzzle, "b", "answer b")
