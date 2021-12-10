from common import getPuzzle, submitSecure
from collections import deque
from functools import reduce
from operator import mul
from itertools import permutations
from collections import Counter
from itertools import accumulate

puzzle = getPuzzle()

rawInput = puzzle.input_data

def parseInput(inp):
    return list(inp.splitlines())

inp = parseInput(rawInput)
print(inp)
# submitSecure(puzzle, "a", "answer a")

# submitSecure(puzzle, "b", "answer b")
