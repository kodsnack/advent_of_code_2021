
from collections import Counter, defaultdict, deque
from functools import reduce
from heapq import heappop, heappush
from itertools import combinations, permutations, product
from helpers import distance, distance_sq, eight_neighs, eight_neighs_bounded, grouped_lines, ints, manhattan, multall, n_neighs, neighs, neighs_bounded


def solve(lines):
    prev = 10**10
    times = 0

    for l in lines:
        if l > prev:
            times += 1
        prev = l

    return times


if __name__ == '__main__':
    lines = []

    with open('1.txt') as f:
        for line in f.readlines():
            lines.append(int(line))

    print(solve(lines))
