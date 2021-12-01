
from collections import Counter, defaultdict, deque
from functools import reduce
from heapq import heappop, heappush
from itertools import combinations, permutations, product
from helpers import distance, distance_sq, eight_neighs, eight_neighs_bounded, grouped_lines, ints, manhattan, multall, n_neighs, neighs, neighs_bounded


def solve(lines):
    return sum(lines[x] > lines[x-1] for x in range(1, len(lines)))

if __name__ == '__main__':
    lines = []

    with open('1.txt') as f:
        for line in f.readlines():
            lines.append(int(line))

    print(solve(lines))
