
from collections import Counter, defaultdict, deque
from functools import reduce
from heapq import heappop, heappush
from itertools import combinations, permutations, product
from helpers import distance, distance_sq, eight_neighs, eight_neighs_bounded, grouped_lines, ints, manhattan, multall, n_neighs, neighs, neighs_bounded


def solve(lines):
    z = 0
    x = 0
    aim = 0

    for move, d in lines:
        val = int(d)

        if move == 'forward':
            x += val
            z += val * aim
        elif move == 'up':
            aim -= val
        else:
            aim += val

    return z*x


if __name__ == '__main__':
    lines = []

    with open('2.txt') as f:
        for line in f.readlines():
            lines.append(line.split())

    print(solve(lines))
