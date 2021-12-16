from collections import Counter, defaultdict, deque
from functools import reduce
from heapq import heappop, heappush
from itertools import combinations, permutations, product
from helpers import chunks, chunks_with_overlap, columns, digits, distance, distance_sq, eight_neighs, eight_neighs_bounded, grouped_lines, ints, manhattan, multall, n_neighs, neighs, neighs_bounded


def solve(hex):
    binary = []

    for d in hex:
        b = bin(int(d, 16))[2:]
        padding = '0' * (4-len(b))
        
        for c in padding+b:
            binary.append(c)

    def parsebin(start, end):
        try:
            return int(''.join(binary[start:end]), 2)
        except:
            return 0

    def parse_packet(startpos):
        version = parsebin(startpos, startpos+3)
        typeid = parsebin(startpos+3, startpos+6)

        startpos += 6

        if typeid == 4:
            vals = []
            while binary[startpos] == '1':
                vals += binary[startpos+1:startpos+5]
                startpos += 5

            vals += binary[startpos+1:startpos+5]
            startpos += 5

            return (int(''.join(vals), 2), startpos)

        startpos += 1

        package_vals = []

        if binary[startpos-1] == '0':
            bitlength = parsebin(startpos, startpos+15)
            startpos += 15
            waspos = startpos

            while startpos - waspos < bitlength:
                value, startpos = parse_packet(startpos)
                package_vals.append(value)

        else:
            packlength = parsebin(startpos, startpos+11)
            startpos += 11
            parsedpacks = 0

            while parsedpacks < packlength:
                value, startpos = parse_packet(startpos)
                package_vals.append(value)
                parsedpacks += 1

        if typeid == 0:
            return (sum(package_vals), startpos)
        if typeid == 1:
            return (multall(package_vals), startpos)
        if typeid == 2:
            return (min(package_vals), startpos)
        if typeid == 3:
            return (max(package_vals), startpos)
        if typeid == 5:
            return (1 if package_vals[0] > package_vals[1] else 0, startpos)
        if typeid == 6:
            return (1 if package_vals[0] < package_vals[1] else 0, startpos)
        if typeid == 7:
            return (1 if package_vals[0] == package_vals[1] else 0, startpos)

    return parse_packet(0)[0]


def main():
    with open('16.txt') as f:
        for line in f.readlines():
            return solve(line.rstrip())


if __name__ == '__main__':
    print(main())
