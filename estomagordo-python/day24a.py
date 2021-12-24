from collections import Counter, defaultdict, deque
from functools import lru_cache, reduce
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

    programettes = list(chunks(instructions, 18))
    n = len(programettes)
    seen = {(0, 0, 0, 0)}

    frontier = deque([(0, 0, 0, 0, '')])

    while True:
        i, x, y, z, word = frontier.popleft()
        if len(seen) % 10**6 == 0:
            print(len(seen), len(frontier))

        if i == n-1:
            for w in range(1, 10):
                _, __, dz = calcfor(w, x, y, z, programettes[i][1:])
                if dz == 0:
                    return word + str(w)
        
        for w in range(9, 0, -1):
            dx, dy, dz = calcfor(w, x, y, z, programettes[i][1:])
            if (i+1, dx, dy, dz) not in seen:
                seen.add((i+1, dx, dy, dz))
                frontier.append((i+1, dx, dy, dz, word+str(w)))


def main():
    lines = []

    with open('24.txt') as f:
        for line in f.readlines():
            lines.append(line.split())
            
    return solve(lines)


if __name__ == '__main__':
    print(main())