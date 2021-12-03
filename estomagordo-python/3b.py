
from collections import Counter, defaultdict, deque
from functools import reduce
from heapq import heappop, heappush
from itertools import combinations, permutations, product
from helpers import distance, distance_sq, eight_neighs, eight_neighs_bounded, grouped_lines, ints, manhattan, multall, n_neighs, neighs, neighs_bounded


def find_oxygen(lines, n):
    for x in range(n):
        if len(lines) == 1:
            break

        newlines = []

        zeroes = 0
        ones = 0

        for line in lines:
            if line[x] == '0':
                zeroes += 1
            else:
                ones += 1

        for line in lines:
            if zeroes > ones:
                if line[x] == '0':
                    newlines.append(line)
            elif line[x] == '1':
                newlines.append(line)

        lines = newlines

    return int(lines[0], 2)


def find_co2(lines, n):
    for x in range(n):
        if len(lines) == 1:
            break

        newlines = []

        zeroes = 0
        ones = 0

        for line in lines:
            if line[x] == '0':
                zeroes += 1
            else:
                ones += 1

        for line in lines:
            if zeroes > ones:
                if line[x] == '1':
                    newlines.append(line)
            elif line[x] == '0':
                newlines.append(line)

        lines = newlines

    return int(lines[0], 2)


def solve(lines):
    n = len(lines[0])

    oxygen = find_oxygen(lines, n)
    co2 = find_co2(lines, n)

    return oxygen*co2


if __name__ == '__main__':
    lines = []

    with open('3.txt') as f:
        for line in f.readlines():
            lines.append(line.rstrip())
            
    print(solve(lines))
