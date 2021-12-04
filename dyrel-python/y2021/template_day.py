from common import getPuzzle, submitSecure

puzzle = getPuzzle()

rawInput = puzzle.input_data

def parseInput(inp):
    return list(inp.splitlines())

inp = parseInput(rawInput)
print(inp)
# submitSecure(puzzle, "a", "answer a")

# submitSecure(puzzle, "b", "answer b")
