from collections import Counter, defaultdict, deque
from functools import reduce
from heapq import heappop, heappush
from itertools import combinations, permutations, product
from helpers import distance, distance_sq, eight_neighs, eight_neighs_bounded, grouped_lines, ints, manhattan, multall, n_neighs, neighs, neighs_bounded, columns


def solve(fish, days):
    seen = {}

    def helper(fishdays, remaining):
        if remaining == 0:
            return 1

        if (fishdays, remaining) in seen:
            return seen[(fishdays, remaining)]

        if fishdays > 0:
            val = helper(fishdays-1, remaining-1)
            seen[(fishdays, remaining)] = val
            return val

        val = helper(6, remaining-1) + helper(8, remaining-1)
        seen[(fishdays, remaining)] = val
        return val

    return sum(helper(f, days) for f in fish)

def main():
    with open('6.txt') as f:
        line = f.readline()            
        fish = ints(line)
        return solve(fish, 256)


if __name__ == '__main__':
    print(main())
