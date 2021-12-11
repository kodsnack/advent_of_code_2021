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

def findProblem(line):
    stack = deque()
    correct = {'(':')', '{':'}', '[':']', '<':'>'}
    for c in line:
        if c in correct:
            stack.append(correct[c])
        elif len(stack) == 0 or c != stack[-1]:
            return c, stack
        else:
            stack.pop()
    return "", stack

autocomp = {")":1, "]": 2, "}": 3, ">": 4}
def calcAutocompScore(stack):
    result = 0
    while len(stack) > 0:
        result = result * 5 + autocomp[stack.pop()]
    return result

mismatch = {")":3, "]": 57, "}": 1197, ">": 25137}
def calcMistmatchScore(c):
    return mismatch[c]

inp = parseInput(rawInput)
mismatch_score = 0
autocomp_scores = []
for line in inp:
    offending_char, stack = findProblem(line)
    if offending_char in mismatch:
        mismatch_score += calcMistmatchScore(offending_char)
    elif offending_char == "":
        autocomp_scores.append(calcAutocompScore(stack))
    else:
        print("Matched!")
        
submitSecure(puzzle, "a", mismatch_score)
submitSecure(puzzle, "b",
             sorted(autocomp_scores)[len(autocomp_scores)//2])
