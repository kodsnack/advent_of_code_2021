from collections import Counter, defaultdict, deque
from functools import reduce
from heapq import heappop, heappush
from itertools import combinations, permutations, product
from helpers import chunks, chunks_with_overlap, columns, digits, distance, distance_sq, eight_neighs, eight_neighs_bounded, grouped_lines, ints, manhattan, multall, n_neighs, neighs, neighs_bounded


def solve(steps):
    cubes = set()

    for on, step in steps:
        lox, hix, loy, hiy, loz, hiz = step
        
        for x in range(max(-50, lox), min(hix+1, 51)):
            for y in range(max(-50, loy), min(hiy+1, 51)):
                for z in range(max(loz, -50), min(hiz+1, 51)):
                    if on:
                        cubes.add((x, y, z))
                    else:
                        cubes.discard((x, y, z))

    return len(cubes)


def main():
    steps = []

    with open('22.txt') as f:
        for line in f.readlines():
            on = line[:2] == 'on'
            nums = ints(line)
            steps.append((on, nums))
            
    return solve(steps)


if __name__ == '__main__':
    print(main())
