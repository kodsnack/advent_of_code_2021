from collections import Counter, defaultdict, deque
from functools import reduce
from heapq import heappop, heappush
from itertools import combinations, permutations, product
from helpers import digits,distance, distance_sq, eight_neighs, eight_neighs_bounded, grouped_lines, ints, manhattan, multall, n_neighs, neighs, neighs_bounded, columns


def solve(lines):
    count = 0
    height = len(lines)
    width = len(lines[0])

    for y in range(height):
        for x in range(width):
            val = lines[y][x]
            small = True
            for ny, nx in neighs_bounded(y, x, 0, height-1, 0, width-1):
                nval = lines[ny][nx]
                if nval <= val:
                    small = False
            if small:
                count += 1+val

    return count


def main():
    lines = []

    with open('9.txt') as f:
        for line in f.readlines():
            lines.append(digits(line))
            
    return solve(lines)


if __name__ == '__main__':
    print(main())
