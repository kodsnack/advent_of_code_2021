from common import getPuzzle, submitSecure

puzzle = getPuzzle()

rawInput = puzzle.input_data

def parseInput(inp):
    l = list()
    for line in inp.splitlines():
        parts = [[], []]
        idx = 0
        for item in line.split():
            if item == '|':
                idx += 1
                continue
            parts[idx].append(''.join(sorted(item)))
        l.append(parts)
    return l

inp = parseInput(rawInput)
count = 0
for item in inp:
    for p in item[1]:
        if len(p) in (2, 4, 3, 7):
            count += 1
submitSecure(puzzle, "a", count)

from itertools import permutations

def mapPermutations(s):
    for perm in permutations(s, len(s)):
        yield {x:y for x, y in zip(s, perm)}

def testMapping(cableMapping, items, segments):
    mapping = dict()
    for item in items:
        mappedItem = ''.join(sorted(list(map(lambda cable:cableMapping[cable],
                                             item))))
        if mappedItem not in segments:
            return mapping
        else:
            mapping[item] = segments[mappedItem]
    return mapping

segments = {'abcefg': 0,
            'cf': 1, 
            'acdeg': 2, 
            'acdfg': 3, 
            'bcdf': 4, 
            'abdfg': 5, 
            'abdefg': 6,
            'acf': 7,
            'abcdefg': 8,
            'abcdfg': 9}
def findmap(items):
    mapping = dict()
    for d in mapPermutations('abcdefg'):
        mapping = testMapping(d, items, segments)
        if len(mapping) == 10:
            return mapping

tot = 0
for line in inp:
    m = findmap(line[0])
    tot += int(''.join(str(m[i]) for i in line[1]))
submitSecure(puzzle, "b", tot)
