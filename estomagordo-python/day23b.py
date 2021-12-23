from collections import Counter, defaultdict, deque
from functools import reduce
from heapq import heappop, heappush
from itertools import combinations, permutations, product
from helpers import chunks, chunks_with_overlap, columns, digits, distance, distance_sq, eight_neighs, eight_neighs_bounded, grouped_lines, ints, manhattan, multall, n_neighs, neighs, neighs_bounded


def solve(lines):
    height = len(lines)
    width = len(lines[0])

    a = []
    b = []
    c = []
    d = []

    open = set()

    for y in range(height):
        for x in range(width):
            if lines[y][x] == 'A':
                a.append((y, x))
            if lines[y][x] == 'B':
                b.append((y, x))
            if lines[y][x] == 'C':
                c.append((y, x))
            if lines[y][x] == 'D':
                d.append((y, x))
            if lines[y][x] != '#':
                open.add((y, x))

    blocking = {(1, 3), (1, 5), (1, 7), (1, 9)}
    goala = [(2, 3), (3, 3), (4, 3), (5, 3)]
    goalb = [(2, 5), (3, 5), (4, 5), (5, 5)]
    goalc = [(2, 7), (3, 7), (4, 7), (5, 7)]
    goald = [(2, 9), (3, 9), (4, 9), (5, 9)]

    a.sort()
    b.sort()
    c.sort()
    d.sort()

    states = [[0, a, b, c, d]]
    seen = {(tuple(a), tuple(b), tuple(c), tuple(d)): 0}
    enseen = {0}

    def tuplify(apos, bpos, cpos, dpos):
        return (tuple(apos), tuple(bpos), tuple(cpos), tuple(dpos))

    def isfree(y, x, apos, bpos, cpos, dpos):
        if (y, x) not in open:
            return False
        if (y, x) in apos:
            return False
        if (y, x) in bpos:
            return False
        if (y, x) in cpos:
            return False
        return (y, x) not in dpos

    while True:
        energy, apos, bpos, cpos, dpos = heappop(states)     
        if energy not in enseen:
            enseen.add(energy)           
            print(energy, len(seen))
        allpos = [apos, bpos, cpos, dpos]

        if apos == goala and bpos == goalb and cpos == goalc and dpos == goald:
            return energy

        blocker = False

        for i, yx in  enumerate(apos):
            y, x = yx
            if (y, x) in blocking:
                blocker = True
                for deltax in (-1, 1):
                    if isfree(y, x+deltax, apos, bpos, cpos, dpos):
                        dapos = sorted(apos[:i] + [(y, x+deltax)] + apos[i+1:])
                        t = tuplify(dapos, bpos, cpos, dpos)
                        if t not in seen or seen[t] > energy+1:
                            seen[t] = energy+1
                            heappush(states, [energy+1, dapos, list(bpos), list(cpos), list(dpos)])
                if x == 3 and isfree(2, 3, apos, bpos, cpos, dpos):
                    containsothers = False
                    
                    for pos in (bpos, cpos, dpos):
                        for dy, dx in pos:
                            if (dy, dx) in ((3, 3), (4, 3), (5, 3)):
                                containsothers = True
                                break

                    if containsothers:
                        continue

                    dapos = sorted(apos[:i] + [(2, 3)] + apos[i+1:])

                    t = tuplify(dapos, bpos, cpos, dpos)
                    if t not in seen or seen[t] > energy+1:
                        seen[t] = energy+1
                        heappush(states, [energy+1, list(dapos), list(bpos), list(cpos), list(dpos)])
        for i, yx in  enumerate(bpos):
            y, x = yx
            if (y, x) in blocking:
                blocker = True
                for deltax in (-1, 1):
                    if isfree(y, x+deltax, apos, bpos, cpos, dpos):
                        dbpos = sorted(bpos[:i] + [(y, x+deltax)] + bpos[i+1:])
                        t = tuplify(apos, dbpos, cpos, dpos)
                        if t not in seen or seen[t] > energy+10:
                            seen[t] = energy+10
                            heappush(states, [energy+10, list(apos), dbpos, list(cpos), list(dpos)])
                if x == 5 and isfree(2, 5, apos, bpos, cpos, dpos):
                    containsothers = False
                    
                    for pos in (apos, cpos, dpos):
                        for dy, dx in pos:
                            if (dy, dx) in ((3, 5), (4, 5), (5, 5)):
                                containsothers = True
                                break

                    if containsothers:
                        continue

                    dbpos = sorted(bpos[:i] + [(2, 5)] + bpos[i+1:])

                    t = tuplify(apos, dbpos, cpos, dpos)
                    if t not in seen or seen[t] > energy+10:
                        seen[t] = energy+10
                        heappush(states, [energy+10, list(apos), list(dbpos), list(cpos), list(dpos)])
        for i, yx in  enumerate(cpos):
            y, x = yx
            if (y, x) in blocking:
                blocker = True
                for deltax in (-1, 1):
                    if isfree(y, x+deltax, apos, bpos, cpos, dpos):
                        dcpos = sorted(cpos[:i] + [(y, x+deltax)] + cpos[i+1:])
                        t = tuplify(apos, bpos, dcpos, dpos)
                        if t not in seen or seen[t] > energy+100:
                            seen[t] = energy+100
                            heappush(states, [energy+100, list(apos), list(bpos), dcpos, list(dpos)])
                if x == 7 and isfree(2, 7, apos, bpos, cpos, dpos):
                    containsothers = False
                    
                    for pos in (apos, bpos, dpos):
                        for dy, dx in pos:
                            if (dy, dx) in ((3, 7), (4, 7), (5, 7)):
                                containsothers = True
                                break

                    if containsothers:
                        continue

                    dcpos = sorted(cpos[:i] + [(2, 3)] + cpos[i+1:])
                    
                    t = tuplify(apos, bpos, dcpos, dpos)
                    if t not in seen or seen[t] > energy+100:
                        seen[t] = energy+100
                        heappush(states, [energy+100, list(apos), list(bpos), list(dcpos), list(dpos)])
        for i, yx in  enumerate(dpos):
            y, x = yx
            if (y, x) in blocking:
                blocker = True
                for deltax in (-1, 1):
                    if isfree(y, x+deltax, apos, bpos, cpos, dpos):
                        ddpos = sorted(dpos[:i] + [(y, x+deltax)] + dpos[i+1:])
                        t = tuplify(apos, bpos, cpos, ddpos)
                        if t not in seen or seen[t] > energy+1000:
                            seen[t] = energy+1000
                            heappush(states, [energy+1000, list(apos), list(bpos), list(cpos), ddpos])
                if x == 9 and isfree(2, 9, apos, bpos, cpos, dpos):
                    containsothers = False
                    
                    for pos in (apos, bpos, cpos):
                        for dy, dx in pos:
                            if (dy, dx) in ((3, 9), (4, 9), (5, 9)):
                                containsothers = True
                                break

                    if containsothers:
                        continue

                    ddpos = sorted(dpos[:i] + [(2, 3)] + dpos[i+1:])
                    
                    t = tuplify(apos, bpos, cpos, ddpos)
                    if t not in seen or seen[t] > energy+1000:
                        seen[t] = energy+1000
                        heappush(states, [energy+1000, list(apos), list(bpos), list(cpos), list(ddpos)])

        if blocker:
            continue

        if apos != goala:
            for i in range(4):
                for dy, dx in neighs(apos[i][0], apos[i][1]):
                    if (dy, dx) not in open:
                        continue
                    if any((dy, dx) in pos for pos in allpos):
                        continue
                    if dy < apos[i][0] and dx == 3:
                        continue
                    if dy > apos[i][0] and dy == 2 and dx != 3:
                        continue
                    dapos = sorted(apos[:i] + [(dy, dx)] + apos[i+1:])
                    t = tuplify(dapos, bpos, cpos, dpos)
                    if t not in seen or seen[t] > energy+1:
                        seen[t] = energy+1
                        heappush(states, [energy+1, list(dapos), list(bpos), list(cpos), list(dpos)])
        if bpos != goalb:
            for i in range(4):
                for dy, dx in neighs(bpos[i][0], bpos[i][1]):
                    if (dy, dx) not in open:
                        continue
                    if any((dy, dx) in pos for pos in allpos):
                        continue
                    if dy < bpos[i][0] and dx == 5:
                        continue
                    if dy > bpos[i][0] and dy == 2 and dx != 5:
                        continue
                    dbpos = sorted(bpos[:i] + [(dy, dx)] + bpos[i+1:])
                    t = tuplify(apos, dbpos, cpos, dpos)
                    if t not in seen or seen[t] > energy+10:
                        seen[t] = energy+10
                        heappush(states, [energy+10, list(apos), list(dbpos), list(cpos), list(dpos)])
        if cpos != goalc:
            for i in range(4):
                for dy, dx in neighs(cpos[i][0], cpos[i][1]):
                    if (dy, dx) not in open:
                        continue
                    if any((dy, dx) in pos for pos in allpos):
                        continue
                    if dy < cpos[i][0] and dx == 7:
                        continue
                    if dy > cpos[i][0] and dy == 2 and dx != 7:
                        continue
                    dcpos = sorted(cpos[:i] + [(dy, dx)] + cpos[i+1:])
                    t = tuplify(apos, bpos, dcpos, dpos)
                    if t not in seen or seen[t] > energy+100:
                        seen[t] = energy+100
                        heappush(states, [energy+100, list(apos), list(bpos), list(dcpos), list(dpos)])
        if dpos != goald:
            for i in range(4):
                for dy, dx in neighs(dpos[i][0], dpos[i][1]):
                    if (dy, dx) not in open:
                        continue
                    if any((dy, dx) in pos for pos in allpos):
                        continue
                    if dy < dpos[i][0] and dx == 9:
                        continue
                    if dy > dpos[i][0] and dy == 2 and dx != 9:
                        continue
                    ddpos = sorted(dpos[:i] + [(dy, dx)] + dpos[i+1:])
                    t = tuplify(apos, bpos, cpos, ddpos)
                    if t not in seen or seen[t] > energy+1000:
                        seen[t] = energy+1000
                        heappush(states, [energy+1000, list(apos), list(bpos), list(cpos), list(ddpos)])


def main():
    width = -1
    extra1 = '  #D#C#B#A#  '
    extra2 = '  #D#B#A#C#  '
    lines = []

    with open('23.txt') as f:
        for line in f.readlines():
            
            if width == -1:
                width = len(line.rstrip())
            
            row = line.rstrip()
            row += ' ' * (width-len(row))
            lines.append(row)

            if len(lines) == 3:
                lines.append(extra1)
                lines.append(extra2)
            
    return solve(lines)


if __name__ == '__main__':
    print(main())
