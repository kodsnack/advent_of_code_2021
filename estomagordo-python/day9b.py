from collections import Counter, defaultdict, deque
from functools import reduce
from heapq import heappop, heappush
from itertools import combinations, permutations, product
from helpers import distance, distance_sq, eight_neighs, eight_neighs_bounded, grouped_lines, ints, manhattan, multall, n_neighs, neighs, neighs_bounded, columns


def solve(lines):    
    height = len(lines)
    width = len(lines[0])

    identified = set()
    basins = []

    for y in range(height):
        for x in range(width):
            val = lines[y][x]
            if val == 9 or (y, x) in identified:
                continue
            basin = {(y, x)}
            frontier = [(y, x)]
            
            for dy, dx in frontier:                
                for ny, nx in neighs_bounded(dy, dx, 0, height-1, 0, width-1):
                    nval = lines[ny][nx]
                    if nval < 9 and (ny, nx) not in basin:
                        basin.add((ny, nx))
                        frontier.append((ny, nx))

            basins.append(len(basin))
            for by, bx in basin:
                identified.add((by, bx))

    basins.sort()
    
    return multall(basins[-3:])


def main():
    lines = []

    with open('9.txt') as f:
        for line in f.readlines():
            l = line.rstrip()
            ll = list(l)
            lines.append(list(map(int, ll)))
            
    return solve(lines)


if __name__ == '__main__':
    print(main())
# 13248