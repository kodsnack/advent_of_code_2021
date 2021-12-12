from common import getPuzzle, submitSecure
from collections import deque, defaultdict

puzzle = getPuzzle()

rawInput = puzzle.input_data

def parseInput(inp):
    caveMap = defaultdict(set)
    for line in inp.splitlines():
        cave1, cave2 = line.split('-')
        caveMap[cave1].add(cave2)
        caveMap[cave2].add(cave1)
    return caveMap

def findAllPaths(caveMap, visitTwice=False):
    allPaths = list()
    bfs = deque()
    reVisited = not visitTwice
    bfs.append((["start"], reVisited))
    while len(bfs) > 0:
        pathSoFar, reVisited = bfs.pop()
        lastCave = pathSoFar[-1]
        if lastCave == "end":
            allPaths.append(pathSoFar)
        else:
            for nextCave in caveMap[lastCave]:
                nextReVisited = reVisited
                if nextCave == "start":
                    continue
                if nextCave.islower() and nextCave in pathSoFar:
                    if reVisited:
                        continue
                    nextReVisited = True
                newPath = pathSoFar[:] + [nextCave]
                bfs.append((newPath, nextReVisited))
    return allPaths

caves = parseInput(rawInput)
submitSecure(puzzle, "a", len(findAllPaths(caves, visitTwice=False)))
submitSecure(puzzle, "b", len(findAllPaths(caves, visitTwice=True)))
