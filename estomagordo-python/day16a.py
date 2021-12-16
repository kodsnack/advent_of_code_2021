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

    total = 0
    pos = 0

    def parsebin(start, end):
        try:
            return int(''.join(binary[start:end]), 2)
        except:
            return 0

    def parse_packet(startpos):
        # if all(c == '0' for c in binary[startpos:]):
        #     return (0, 0)

        version = parsebin(startpos, startpos+3)
        typeid = parsebin(startpos+3, startpos+6)

        startpos += 6

        if typeid == 4:
            while binary[startpos] == '1':
                startpos += 5

            startpos += 5

            return (version, startpos)

        startpos += 1

        if binary[startpos-1] == '0':
            bitlength = parsebin(startpos, startpos+15)
            startpos += 15
            waspos = startpos

            while startpos - waspos < bitlength:
                subversion, startpos = parse_packet(startpos)
                version += subversion

        else:
            packlength = parsebin(startpos, startpos+11)
            startpos += 11
            parsedpacks = 0

            while parsedpacks < packlength:
                subversion, startpos = parse_packet(startpos)
                version += subversion
                parsedpacks += 1

        return (version, startpos)

    while pos < len(binary):
        version, pos = parse_packet(pos)
        total += version

        if all(c == '0' for c in binary[pos:]):
            break

    return total


def main():
    with open('16.txt') as f:
        for line in f.readlines():
            return solve(line.rstrip())


if __name__ == '__main__':
    print(main())
