from collections import Counter, defaultdict, deque
from functools import reduce
from heapq import heappop, heappush
from itertools import combinations, permutations, product
from helpers import distance, distance_sq, eight_neighs, eight_neighs_bounded, grouped_lines, ints, manhattan, multall, n_neighs, neighs, neighs_bounded, columns


def solve(lines):
    best = (10**10,-1)

    for val in range(min(lines), max(lines)):
        cost = 0

        for crab in lines:
            d = abs(crab-val)
            cost += (d*(d+1))//2

        best = min(best, (cost,val))

    return best[0]


def main():
    with open('7.txt') as f:
        for line in f.readlines():
            return solve(ints(line))


if __name__ == '__main__':
    print(main())