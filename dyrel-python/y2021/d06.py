from common import getPuzzle, submitSecure
from collections import Counter

puzzle = getPuzzle()

rawInput = puzzle.input_data

def parseInput(inp):
    return Counter(map(int, inp.split(",")))

def newGeneration(gen):
    ng = Counter({k-1:v for k,v in gen.items()})
    ng[8] = ng[-1]
    ng[6] += ng[-1]
    del ng[-1]
    return ng

gen = parseInput(rawInput)
for i in range(80):
    gen = newGeneration(gen)
submitSecure(puzzle, "a", sum(gen.values()))
for i in range(256-80):
    gen = newGeneration(gen)
submitSecure(puzzle, "b", sum(gen.values()))
