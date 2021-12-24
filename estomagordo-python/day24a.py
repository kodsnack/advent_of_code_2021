from collections import Counter, defaultdict, deque
from functools import reduce
from heapq import heappop, heappush
from itertools import combinations, permutations, product
from helpers import chunks, chunks_with_overlap, columns, digits, distance, distance_sq, eight_neighs, eight_neighs_bounded, grouped_lines, ints, manhattan, multall, n_neighs, neighs, neighs_bounded


def isnum(s):
    return s.isdigit() or (s[0] == '-' and s[1:].isdigit())

def solve(instructions):
    def isvalid(mid, inst):
        pos = 0
        values = defaultdict(int)

        for i, ins in enumerate(inst):
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
                values[a] = 1 if values[a] == val else 0
        
        return values['z'] == 0

    # seen = {}

    def calcfor(w, x, y, z, chunk):
        values = {'w': w, 'x': x, 'y': y, 'z': z}

        # t = (w, x, y, z, chunk)

        # if t in seen:
        #     return seen[]

        for ins in chunk:
            command = ins[0]
            
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
                values[a] = 1 if (values[a] == val) else 0
        
        return (values['x'], values['y'], values['z'])

    outcomes = []

    for i, chunk in enumerate(chunks(instructions, 18)):
        print(i, len(outcomes))
        chunkout = set()

        if i == 0:
            for w in range(1, 10):                
                retx, rety, retz = calcfor(w, 0, 0, 0, chunk)
                chunkout.add((str(w), retx, rety, retz))
        else:
            for sw, x, y, z in outcomes:
                for w in range(1, 10):
                    retx, rety, retz = calcfor(w, x, y, z, chunk)
                    chunkout.add((sw + str(w), retx, rety, retz))

        outcomes = chunkout
    
    return max(oc[0] for oc in outcomes if oc[-1] == 0)

    # res = ''
    
    # for chunk in chunks(instructions, 18):
    #     for val in range(9, 0, -1):
    #         if isvalid(val, chunk):
    #             res += str(val)
    #             break

    # return ''.join(res)
    
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

        if isvalid(mid, instructions):
            largest = max(largest, mid)
            print('best', mid)
            lo = mid+1
        else:
            print('fails', mid)
            hi = mid-1

    return largest


def main():
    lines = []

    with open('24.txt') as f:
        for line in f.readlines():
            lines.append(line.split())
            
    return solve(lines)


if __name__ == '__main__':
    print(main())
