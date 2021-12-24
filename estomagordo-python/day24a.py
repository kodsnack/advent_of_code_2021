from collections import Counter, defaultdict, deque
from functools import reduce
from heapq import heappop, heappush
from itertools import combinations, permutations, product
from helpers import chunks, chunks_with_overlap, columns, digits, distance, distance_sq, eight_neighs, eight_neighs_bounded, grouped_lines, ints, manhattan, multall, n_neighs, neighs, neighs_bounded


def isnum(s):
    return s.isdigit() or (s[0] == '-' and s[1:].isdigit())

def solve(instructions):
    def isvalid(mid):
        pos = 0
        values = defaultdict(int)

        for i, ins in enumerate(instructions):
            command = ins[0]

            if command == 'inp':
                arg = ins[1]
                values[arg] = int(str(mid)[pos])
                pos += 1
            if command == 'add':
                a, b = ins[1:]
                val = int(b) if isnum(b) else values[b]
                values[a] += val
            if command == 'mul':
                a, b = ins[1:]
                val = int(b) if isnum(b) else values[b]
                values[a] *= val
            if command == 'div':
                a, b = ins[1:]
                val = int(b) if isnum(b) else values[b]
                values[a] //= val
            if command == 'mod':
                a, b = ins[1:]
                val = int(b) if isnum(b) else values[b]
                values[a] %= val
            if command == 'eql':
                a, b = ins[1:]
                val = int(b) if isnum(b) else values[b]
                values[a] = 1 if a == val else 0
        
        return values['z'] == 0
    
    largest = 0
    lo = 11111111111111
    hi = 99999999999999

    # for num in range(hi, 0, -1):
    #     if not '0' in str(num):
    #         res = isvalid(num)
    #         if not res:
    #             print(num)

    while lo < hi:
        mid = (lo+hi)//2

        if '0' in str(mid):
            print('zeroes', mid)    
            s = str(mid)

            for pos in range(len(s)):
                if s[pos] == '0':
                    s = s[:pos] + '1' + s[pos+1:]

            mid = int(s)

        if isvalid(mid):
            largest = max(largest, mid)
            print('best', mid)
            lo = mid+1
        else:
            print('fails', mid)
            hi = mid-1


def main():
    lines = []

    with open('24.txt') as f:
        for line in f.readlines():
            lines.append(line.split())
            
    return solve(lines)


if __name__ == '__main__':
    print(main())
