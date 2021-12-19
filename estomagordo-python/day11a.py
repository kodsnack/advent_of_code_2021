from collections import Counter, defaultdict, deque
from functools import reduce
from heapq import heappop, heappush
from itertools import combinations, permutations, product
from helpers import columns, digits, distance, distance_sq, eight_neighs, eight_neighs_bounded, grouped_lines, ints, manhattan, multall, n_neighs, neighs, neighs_bounded


def solve(lines, steps=100):
    count = 0

    for _ in range(steps):
        flashing = set()

        for y in range(10):
            for x in range(10):
                lines[y][x] += 1

        while True:
            keep = False
            for y in range(10):
                for x in range(10):
                    if lines[y][x] > 9 and (y, x) not in flashing:
                        flashing.add((y, x))
                        count += 1
                        keep = True
                        for ny, nx in eight_neighs_bounded(y, x, 0, 9, 0, 9):
                            lines[ny][nx] += 1
            if not keep:
                break

        for y, x in flashing:
            lines[y][x] = 0

    return count


def main():
    lines = []

    with open('11.txt') as f:
        for line in f.readlines():
            lines.append(digits(line))
            
    return solve(lines)


if __name__ == '__main__':
    print(main())
