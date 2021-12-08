from collections import Counter, defaultdict, deque
from functools import reduce
from heapq import heappop, heappush
from itertools import combinations, permutations, product
from helpers import distance, distance_sq, eight_neighs, eight_neighs_bounded, grouped_lines, ints, manhattan, multall, n_neighs, neighs, neighs_bounded, columns


def solve(lines):
    count = 0

    for line in lines:
        hasseen = False
        for val in line:
            if val == '|':
                hasseen = True
            elif hasseen:
                if len(val) in (2,3,4,7):
                    count += 1

    return count


def main():
    lines = []

    with open('8.txt') as f:
        for line in f.readlines():
            vals = line.split()            
            lines.append(vals)
            
    return solve(lines)


if __name__ == '__main__':
    print(main())