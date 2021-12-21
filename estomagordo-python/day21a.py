from collections import Counter, defaultdict, deque
from functools import reduce
from heapq import heappop, heappush
from itertools import combinations, permutations, product
from helpers import chunks, chunks_with_overlap, columns, digits, distance, distance_sq, eight_neighs, eight_neighs_bounded, grouped_lines, ints, manhattan, multall, n_neighs, neighs, neighs_bounded


def solve(lines):
    a = 4
    b = 10

    d = 1
    dsize = 100
    rolls = 0
    scora = 0 
    scorb = 0
    arolling = True
    goal = 1000
    size = 10
    moves = 3
    c = Counter()

    while scora < goal and scorb < goal:
        if arolling:
            for _ in range(moves):
                rolls += 1
                a += d
                if a > size:
                    if a % size == 0:
                        a = size
                    else:
                        a %= size
                d += 1
                if d > dsize:
                    d = 1

            scora += a
            c[a] += 1
        else :
            for _ in range(moves):
                rolls += 1
                b += d
                if b > size:
                    if b % size == 0:
                        b = size
                    else:
                        b %= size
                d += 1
                if d > dsize:
                    d = 1

            scorb += b
            c[b] += 1
        arolling = not arolling

    return min(scora, scorb) * rolls


def main():
    lines = []

    with open('21.txt') as f:
        for line in f.readlines():
            lines.append(line)
            
    return solve(lines)


if __name__ == '__main__':
    print(main())
