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
    goala = [(2, 3), (3, 3)]
    goalb = [(2, 5), (3, 5)]
    goalc = [(2, 7), (3, 7)]
    goald = [(2, 9), (3, 9)]

    a.sort()
    b.sort()
    c.sort()
    d.sort()

    states = [[0, a, b, c, d]]
    seen = {(tuple(a), tuple(b), tuple(c), tuple(d)): 0}

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
                        dapos = []
                        if i == 0:
                            dapos = sorted([(y, x+deltax), apos[1]])
                        else:
                            dapos = sorted([(y, x+deltax), apos[0]])
                        t = tuplify(dapos, bpos, cpos, dpos)
                        if t not in seen or seen[t] > energy+1:
                            seen[t] = energy+1
                            heappush(states, [energy+1, dapos, list(bpos), list(cpos), list(dpos)])
                if x == 3 and isfree(2, 3, apos, bpos, cpos, dpos):
                    if not isfree(3, 3, apos, bpos, cpos, dpos) and not (3, 3) in apos:
                        continue
                    dapos = []
                    if i == 0:
                        dapos = sorted([(2, 3), apos[1]])
                    else:
                        dapos = sorted([(2, 3), apos[0]])
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
                        dbpos = []
                        if i == 0:
                            dbpos = sorted([(y, x+deltax), bpos[1]])
                        else:
                            dbpos = sorted([(y, x+deltax), bpos[0]])
                        t = tuplify(apos, dbpos, cpos, dpos)
                        if t not in seen or seen[t] > energy+10:
                            seen[t] = energy+10
                            heappush(states, [energy+10, list(apos), dbpos, list(cpos), list(dpos)])
                if x == 5 and isfree(2, 5, apos, bpos, cpos, dpos):
                    if not isfree(3, 5, apos, bpos, cpos, dpos) and not (3, 5) in bpos:
                        continue
                    dbpos = []
                    if i == 0:
                        dbpos = sorted([(2, 5), bpos[1]])
                    else:
                        dbpos = sorted([(2, 5), bpos[0]])
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
                        dcpos = []
                        if i == 0:
                            dcpos = sorted([(y, x+deltax), cpos[1]])
                        else:
                            dcpos = sorted([(y, x+deltax), cpos[0]])
                        t = tuplify(apos, bpos, dcpos, dpos)
                        if t not in seen or seen[t] > energy+100:
                            seen[t] = energy+100
                            heappush(states, [energy+100, list(apos), list(bpos), dcpos, list(dpos)])
                if x == 7 and isfree(2, 7, apos, bpos, cpos, dpos):
                    if not isfree(3, 7, apos, bpos, cpos, dpos) and not (3, 7) in cpos:
                        continue
                    dcpos = []
                    if i == 0:
                        dcpos = sorted([(2, 7), cpos[1]])
                    else:
                        dcpos = sorted([(2, 7), cpos[0]])
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
                        ddpos = []
                        if i == 0:
                            ddpos = sorted([(y, x+deltax), dpos[1]])
                        else:
                            ddpos = sorted([(y, x+deltax), dpos[0]])
                        t = tuplify(apos, bpos, cpos, ddpos)
                        if t not in seen or seen[t] > energy+1000:
                            seen[t] = energy+1000
                            heappush(states, [energy+1000, list(apos), list(bpos), list(cpos), ddpos])
                if x == 9 and isfree(2, 9, apos, bpos, cpos, dpos):
                    if not isfree(3, 9, apos, bpos, cpos, dpos) and not (3, 9) in dpos:
                        continue
                    ddpos = []
                    if i == 0:
                        ddpos = sorted([(2, 9), dpos[1]])
                    else:
                        ddpos = sorted([(2, 9), dpos[0]])
                    t = tuplify(apos, bpos, cpos, ddpos)
                    if t not in seen or seen[t] > energy+1000:
                        seen[t] = energy+1000
                        heappush(states, [energy+1000, list(apos), list(bpos), list(cpos), list(ddpos)])

        if blocker:
            continue

        if apos != goala:
            for i in range(2):
                for dy, dx in neighs(apos[i][0], apos[i][1]):
                    if (dy, dx) not in open:
                        continue
                    if any((dy, dx) in pos for pos in allpos):
                        continue
                    if (dy, dx) == (2, 3) and (apos[i][0], apos[i][1]) == (3, 3):
                        continue
                    if (dy, dx) == (2, 5) and (apos[i][0], apos[i][1]) != (3, 5):
                        continue
                    if (dy, dx) == (2, 7) and (apos[i][0], apos[i][1]) != (3, 7):
                        continue
                    if (dy, dx) == (2, 9) and (apos[i][0], apos[i][1]) != (3, 9):
                        continue
                    dapos = []
                    if i == 0:
                        dapos = sorted([(dy, dx), apos[1]])
                    else:
                        dapos = sorted([(dy, dx), apos[0]])
                    t = tuplify(dapos, bpos, cpos, dpos)
                    if t not in seen or seen[t] > energy+1:
                        seen[t] = energy+1
                        heappush(states, [energy+1, list(dapos), list(bpos), list(cpos), list(dpos)])
        if bpos != goalb:
            for i in range(2):
                for dy, dx in neighs(bpos[i][0], bpos[i][1]):
                    if (dy, dx) not in open:
                        continue
                    if any((dy, dx) in pos for pos in allpos):
                        continue
                    if (dy, dx) == (2, 3) and (bpos[i][0], bpos[i][1]) != (3, 3):
                        continue
                    if (dy, dx) == (2, 5) and (bpos[i][0], bpos[i][1]) == (3, 5):
                        continue
                    if (dy, dx) == (2, 7) and (bpos[i][0], bpos[i][1]) != (3, 7):
                        continue
                    if (dy, dx) == (2, 9) and (bpos[i][0], bpos[i][1]) != (3, 9):
                        continue
                    dbpos = []
                    if i == 0:
                        dbpos = sorted([(dy, dx), bpos[1]])
                    else:
                        dbpos = sorted([(dy, dx), bpos[0]])
                    t = tuplify(apos, dbpos, cpos, dpos)
                    if t not in seen or seen[t] > energy+10:
                        seen[t] = energy+10
                        heappush(states, [energy+10, list(apos), list(dbpos), list(cpos), list(dpos)])
        if cpos != goalc:
            for i in range(2):
                for dy, dx in neighs(cpos[i][0], cpos[i][1]):
                    if (dy, dx) not in open:
                        continue
                    if any((dy, dx) in pos for pos in allpos):
                        continue
                    if (dy, dx) == (2, 3) and (cpos[i][0], cpos[i][1]) != (3, 3):
                        continue
                    if (dy, dx) == (2, 5) and (cpos[i][0], cpos[i][1]) != (3, 5):
                        continue
                    if (dy, dx) == (2, 7) and (cpos[i][0], cpos[i][1]) == (3, 7):
                        continue
                    if (dy, dx) == (2, 9) and (cpos[i][0], cpos[i][1]) != (3, 9):
                        continue
                    dcpos = []
                    if i == 0:
                        dcpos = sorted([(dy, dx), cpos[1]])
                    else:
                        dcpos = sorted([(dy, dx), cpos[0]])
                    t = tuplify(apos, bpos, dcpos, dpos)
                    if t not in seen or seen[t] > energy+100:
                        seen[t] = energy+100
                        heappush(states, [energy+100, list(apos), list(bpos), list(dcpos), list(dpos)])
        if dpos != goald:
            for i in range(2):
                for dy, dx in neighs(dpos[i][0], dpos[i][1]):
                    if (dy, dx) not in open:
                        continue
                    if any((dy, dx) in pos for pos in allpos):
                        continue
                    if (dy, dx) == (2, 3) and (dpos[i][0], dpos[i][1]) != (3, 3):
                        continue
                    if (dy, dx) == (2, 5) and (dpos[i][0], dpos[i][1]) != (3, 5):
                        continue
                    if (dy, dx) == (2, 7) and (dpos[i][0], dpos[i][1]) != (3, 7):
                        continue
                    if (dy, dx) == (2, 9) and (dpos[i][0], dpos[i][1]) == (3, 9):
                        continue
                    ddpos = []
                    if i == 0:
                        ddpos = sorted([(dy, dx), dpos[1]])
                    else:
                        ddpos = sorted([(dy, dx), dpos[0]])
                    t = tuplify(apos, bpos, cpos, ddpos)
                    if t not in seen or seen[t] > energy+1000:
                        seen[t] = energy+1000
                        heappush(states, [energy+1000, list(apos), list(bpos), list(cpos), list(ddpos)])


def main():
    width = -1
    lines = []

    with open('23.txt') as f:
        for line in f.readlines():
            
            if width == -1:
                width = len(line.rstrip())
            
            row = line.rstrip()
            row += ' ' * (width-len(row))
            lines.append(row)
            
    return solve(lines)


if __name__ == '__main__':
    print(main())
