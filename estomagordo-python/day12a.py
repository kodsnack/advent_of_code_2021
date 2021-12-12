from collections import Counter, defaultdict, deque
from functools import reduce
from heapq import heappop, heappush
from itertools import combinations, permutations, product
from helpers import columns, digits, distance, distance_sq, eight_neighs, eight_neighs_bounded, grouped_lines, ints, manhattan, multall, n_neighs, neighs, neighs_bounded


def solve(lines):
    graph = defaultdict(list)

    for a,b in lines:
        graph[a].append(b)
        graph[b].append(a)

    paths = set()
    frontier = [['start']]

    for path in frontier:
        if path[-1] == 'end':
            paths.add(tuple(path))
            continue

        for node in graph[path[-1]]:
            if node[0].islower() and node in path:
                continue

            frontier.append(path + [node])

    return len(paths)


def main():
    lines = []

    with open('12.txt') as f:
        for line in f.readlines():
            lines.append(line.rstrip().split('-'))
            
    return solve(lines)


if __name__ == '__main__':
    print(main())
