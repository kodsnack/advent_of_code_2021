from os import path
from sys import argv

dayfile = lambda day: f"""from collections import Counter, defaultdict, deque
from functools import reduce
from heapq import heappop, heappush
from itertools import combinations, permutations, product
from helpers import chunks, chunks_with_overlap, columns, digits, distance, distance_sq, eight_neighs, eight_neighs_bounded, grouped_lines, ints, manhattan, multall, n_neighs, neighs, neighs_bounded


def solve(lines):
    pass


def main():
    lines = []

    with open('{day}.txt') as f:
        for line in f.readlines():
            lines.append(line)
            
    return solve(lines)


if __name__ == '__main__':
    print(main())
"""

if __name__ == '__main__':
    day = argv[1]
    
    daya = f'day{day}a.py'
    dayb = f'day{day}b.py'
    inp = f'{day}.txt'

    if not path.isfile(daya):
        with open(daya, 'w') as g:
            g.write(dayfile(day))
    if not path.isfile(dayb):
        with open(dayb, 'w') as g:
            g.write(dayfile(day))
    if not path.isfile(inp):
        with open(inp, 'w') as g:
            g.write('')