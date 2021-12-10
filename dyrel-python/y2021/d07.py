from common import getPuzzle, submitSecure

puzzle = getPuzzle()

rawInput = puzzle.input_data

def parseInput(inp):
    return list(map(int, inp.split(",")))

def fuel1(x, y):
    return abs(x-y)

def fuel2(x, y):
    diff = abs(x-y)
    return diff*(diff+1)//2

def minFuel(inp, calc):
    mini, maxi = min(inp), max(inp)
    return min(sum(calc(x, i)
                   for x in inp)
               for i in range(mini, maxi))

inp = parseInput(rawInput)
submitSecure(puzzle, "a", minFuel(inp, fuel1))
submitSecure(puzzle, "a", minFuel(inp, fuel2))
