from collections import Counter, defaultdict, deque
from functools import reduce
from heapq import heappop, heappush
from itertools import combinations, permutations, product
from helpers import distance, distance_sq, eight_neighs, eight_neighs_bounded, grouped_lines, ints, manhattan, multall, n_neighs, neighs, neighs_bounded, columns


def solve(lines):
    points = defaultdict(int)

    for x1, y1, x2, y2 in lines:
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2)+1):
                points[(x1, y)] += 1
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2)+1):
                points[(x, y1)] += 1
        elif x2 > x1:
            d = x2-x1
            ysign = 1 if y2 > y1 else -1
            for i in range(d+1):
                points[(x1+i, y1+(i*ysign))] += 1
        else:
            d = x1-x2
            ysign = 1 if y2 > y1 else -1
            for i in range(d+1):
                points[(x1-i, y1+(i*ysign))] += 1

    return len([v for v in points.values() if v > 1])


def main():
    lines = []

    with open('5.txt') as f:
        for line in f.readlines():
            lines.append(ints(line))
            
    return solve(lines)


if __name__ == '__main__':
    print(main())