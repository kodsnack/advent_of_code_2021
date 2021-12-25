from collections import Counter, defaultdict, deque
from functools import reduce
from heapq import heappop, heappush
from itertools import combinations, permutations, product
from helpers import chunks, chunks_with_overlap, columns, digits, distance, distance_sq, eight_neighs, eight_neighs_bounded, grouped_lines, ints, manhattan, multall, n_neighs, neighs, neighs_bounded


def solve(lines):
    height = len(lines)
    width = len(lines[0])

    down = set()
    right = set()

    for y in range(height):
        for x in range(width):
            if lines[y][x] == '>':
                right.add((y, x))
            elif lines[y][x] == 'v':
                down.add((y, x))

    steps = 0
    while True:
        newright = set()
        newdown = set()

        for y, x in right:
            if x == width-1:
                if (y, 0) not in down and (y, 0) not in right and (y, 0) not in newright:
                    newright.add((y, 0))
            else:
                if (y, x+1) not in down and (y, x+1) not in right and (y, x+1) not in newright:
                    newright.add((y, x+1))

        for y, x in newright:
            right.add((y, x))
            if x == 0:
                right.remove((y, width-1))
            else:
                right.remove((y, x-1))

        for y, x in down:
            if y == height-1:
                if (0, x) not in down and (0, x) not in right and (0, x) not in newright and (0, x) not in newdown:
                    newdown.add((0, x))
            else:
                if (y+1, x) not in down and (y+1, x) not in right and (y+1, x) not in newright and (y+1, x) not in newdown:
                    newdown.add((y+1, x))

        if not newright and not newdown:
            break

        for y, x in newdown:
            down.add((y, x))
            if y == 0:
                down.remove((height-1, x))
            else:
                down.remove((y-1, x))
        
        steps += 1

    return steps


def main():
    lines = []

    with open('25.txt') as f:
        for line in f.readlines():
            lines.append(line.rstrip())
            
    return solve(lines)


if __name__ == '__main__':
    print(main())
