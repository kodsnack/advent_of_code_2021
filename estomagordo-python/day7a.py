from collections import Counter, defaultdict, deque
from functools import reduce
from heapq import heappop, heappush
from itertools import combinations, permutations, product
from helpers import distance, distance_sq, eight_neighs, eight_neighs_bounded, grouped_lines, ints, manhattan, multall, n_neighs, neighs, neighs_bounded, columns


def solve(crabs):
    lookat = range(min(crabs), max(crabs))
    return min(sum(abs(crab-pos) for crab in crabs) for pos in lookat)


def main():
    with open('7.txt') as f:
        for line in f.readlines():
            return solve(ints(line))


if __name__ == '__main__':
    print(main())