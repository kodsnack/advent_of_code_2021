from common import getPuzzle, submitSecure
from collections import Counter

puzzle = getPuzzle()

rawInput = puzzle.input_data

def parseInput(inp):
    d = dict()
    lines = inp.splitlines()
    start = [c1+c2 for c1, c2 in zip(lines[0][:-1], lines[0][1:])]
    for line in lines[2:]:
        a, _, b = line.split()
        d[a] = (a[0]+b, b+a[1])
    return start, d

def stepPolymers(freq, mapping):
    nextFreq = Counter()
    for item, occur in freq.items():
        nextFreq[mapping[item][0]] += occur
        nextFreq[mapping[item][1]] += occur
    return nextFreq

def countElements(freq, lastItem):
    count = Counter()
    for item, occur in freq.items():
        count[item[0]] += occur
    count[lastItem] += 1
    mostCommon = count.most_common()
    return mostCommon[0][1] - mostCommon[-1][1]

xl, d = parseInput(rawInput)
lastElement = xl[-1][1]
freq = Counter(xl)
for i in range(10):
    freq = stepPolymers(freq, d)
submitSecure(puzzle, "a", countElements(freq, last))
for i in range(40-10):
    freq = stepPolymers(freq, d)
submitSecure(puzzle, "b", countElements(freq, last))
