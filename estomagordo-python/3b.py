
from collections import Counter, defaultdict, deque
from functools import reduce
from heapq import heappop, heappush
from itertools import combinations, permutations, product
from helpers import distance, distance_sq, eight_neighs, eight_neighs_bounded, grouped_lines, ints, manhattan, multall, n_neighs, neighs, neighs_bounded


def find_generic(lines, n, inverted=False):
    for x in range(n):        
        mostlyzeroes = sum(line[x] == '0' for line in lines) * 2 > len(lines)
        xored = inverted^mostlyzeroes
        lines = lines if len(lines) == 1 else [line for line in lines if (line[x] == '1')^xored]

    return int(lines[0], 2)


def find_oxygen(lines, n):    
    return find_generic(lines, n)


def find_co2(lines, n):
    return find_generic(lines, n, True)


def solve(lines):
    n = len(lines[0])
    oxygen = find_oxygen(lines, n)
    co2 = find_co2(lines, n)

    return oxygen*co2


if __name__ == '__main__':
    lines = []

    with open('3.txt') as f:
        for line in f.readlines():
            lines.append(line.rstrip())
            
    print(solve(lines))
