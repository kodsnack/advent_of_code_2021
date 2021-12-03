
from collections import Counter, defaultdict, deque
from functools import reduce
from heapq import heappop, heappush
from itertools import combinations, permutations, product
from helpers import distance, distance_sq, eight_neighs, eight_neighs_bounded, grouped_lines, ints, manhattan, multall, n_neighs, neighs, neighs_bounded


def solve(lines):
    n = len(lines[0])

    gammadigs = ''

    for x in range(n):
        ones = 0
        zeroes = 0

        for line in lines:
            if line[x] == '0':
                zeroes += 1
            else:
                ones += 1

        if ones > zeroes:
            gammadigs += '1'
        else:
            gammadigs += '0'

    gamma = int(gammadigs, 2)
    epsilon = 2**n - 1 - gamma

    return gamma*epsilon


if __name__ == '__main__':
    lines = []

    with open('3.txt') as f:
        for line in f.readlines():
            lines.append(line.rstrip())
            
    print(solve(lines))
