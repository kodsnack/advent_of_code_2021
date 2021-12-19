from collections import Counter, defaultdict, deque
from functools import reduce
from heapq import heappop, heappush
from itertools import combinations, permutations, product
from helpers import chunks, chunks_with_overlap, columns, digits, distance, distance_sq, eight_neighs, eight_neighs_bounded, grouped_lines, ints, manhattan, multall, n_neighs, neighs, neighs_bounded


def solve(lines):
    height = len(lines)
    width = len(lines[0])

    frontier = [(0, 0, 0)]
    seen = {(0, 0): 0}

    while True:
        score, y, x = heappop(frontier)

        if y == height-1 and x == width-1:
            return score

        for ny, nx in neighs_bounded(y, x, 0, height-1, 0, width-1):
            newscore = score+lines[ny][nx]
            if (ny, nx) not in seen or seen[(ny, nx)] > newscore:
                seen[(ny, nx)] = newscore
                heappush(frontier, (newscore, ny, nx))


def main():
    lines = []

    with open('15.txt') as f:
        for line in f.readlines():
            lines.append(digits(line))
            
    return solve(lines)


if __name__ == '__main__':
    print(main())
