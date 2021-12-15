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

    def find(visited, node):
        if node == 'end':
            return 1

        count = 0

        for following in graph[node]:
            if following.isupper():
                count += find(visited, following)
            elif following != 'start' and following not in visited:
                visited.add(following)
                count += find(visited, following)
                visited.remove(following)

        return count

    return find({'start'}, 'start')


def main():
    lines = []

    with open('12.txt') as f:
        for line in f.readlines():
            lines.append(line.rstrip().split('-'))
            
    return solve(lines)


if __name__ == '__main__':
    print(main())
