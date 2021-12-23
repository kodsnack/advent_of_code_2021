from collections import Counter, defaultdict, deque
from functools import reduce
from heapq import heappop, heappush
from itertools import combinations, permutations, product
from helpers import chunks, chunks_with_overlap, columns, digits, distance, distance_sq, eight_neighs, eight_neighs_bounded, grouped_lines, ints, manhattan, multall, n_neighs, neighs, neighs_bounded


def scorepos(j, pos):
    score = 0

    for i, yx in enumerate(pos):
        y, x = yx

        if x == 3 + j*2:
            score += abs(y-(i+2)) * 10**j
        else:
            score += (y-1 + abs(x-(3 + j*2)) + i + 1) * 10**j

    return score


def heuristic(apos, bpos, cpos, dpos):
    count = 0
    allpos = [apos, bpos, cpos, dpos]

    for j, pos in enumerate(allpos):
        count += min(scorepos(j, p) for p in permutations(pos))            

    return count


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

    exampleoptimalpassing = {3000,3010,3050,3080,3088,3688,4288,4328,9328,9378,9438,9508,10108,10113,19113,19153,30153,34153,34157,34161,41161,41169,44169}

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
        
    states = [[heuristic(a, b, c, d), 0, a, b, c, d]]
    seen = {(tuple(a), tuple(b), tuple(c), tuple(d)): 0}
    # enseen = Counter([0])
    enset = {0}

    while True:
        h, energy, apos, bpos, cpos, dpos, = heappop(states)     
        # if energy in exampleoptimalpassing and energy not in enseen:            
        #     print(energy, len(seen))
        #     if energy == 19153:
        #         for val in exampleoptimalpassing:
        #             print(val, enseen[val])
        # enseen[energy] += 1        
        
        if energy not in enset:
            print(h, energy, len(seen))
            enset.add(energy)
        
        allpos = [apos, bpos, cpos, dpos]

        if h == energy:
            return energy

        def explore(pos, i, j, y, x, steps):
            dpos = sorted(pos[:j] + [(y, x)] + pos[j+1:])
            dapos, dbpos, dcpos, ddpos = allpos[:i] + [dpos] + allpos[i+1:]
            t = tuplify(dapos, dbpos, dcpos, ddpos)
            neweng = energy + steps*(10**i)
            
            if t not in seen or seen[t] > neweng:
                seen[t] = neweng
                dh = heuristic(dapos, dbpos, dcpos, ddpos)
                heappush(states, [dh+neweng, neweng, dapos, dbpos, dcpos, ddpos])

        for i, pos in enumerate(allpos):
            rightcol = 3 + 2*i
            otherrightcols = {3 + 2*k for k in range(4)} - {rightcol}

            for j, yx in enumerate(pos):
                y, x = yx

                if x == rightcol:
                    hasbelow = False
                    for dy in range(y+1, 6):
                        if hasbelow:
                            break
                        for posindex in range(4):
                            if posindex == i:
                                continue
                            if any(p == (dy, x) for p in allpos[posindex]):
                                hasbelow = True
                                break

                    if not hasbelow:
                        dy = y
                        
                        while isfree(dy+1, x, apos, bpos, cpos, dpos) and dy < 4:
                            dy += 1

                        if dy > y:
                            explore(pos, i, j, dy, x, dy-y)

                        continue

                    canmoveup = True

                    for dy in range(1, y):
                        if not isfree(dy, x, apos, bpos, cpos, dpos):
                            canmoveup = False
                            break

                    if not isfree(1, x-1, apos, bpos, cpos, dpos) and not isfree(1, x+1, apos, bpos, cpos, dpos):
                        canmoveup = False

                    if not canmoveup:
                        continue

                    right = [dx for dx in range(x+1, 12)]
                    left = [dx for dx in range(x-1, 0, -1)]
                    
                    for direction in (right, left):
                        for dx in direction:
                            if not isfree(1, dx, apos, bpos, cpos, dpos):
                                break

                            if dx not in otherrightcols:
                                explore(pos, i, j, 1, dx, abs(dx-x) + (y-1))
                else:
                    hasbelow = False
                    
                    for dy in range(2, 6):
                        if hasbelow:
                            break
                        for posindex in range(4):
                            if posindex == i:
                                continue
                            if any(p == (dy, rightcol) for p in allpos[posindex]):
                                hasbelow = True
                                break

                    if y == 1:
                        direction = [dx for dx in range(x+1, rightcol+1)] if x < rightcol else [dx for dx in range(x-1, rightcol-1, -1)]
                        valid = True

                        for dx in direction:
                            if not isfree(y, dx, apos, bpos, cpos, dpos):
                                valid = False
                                break

                        if not valid:
                            continue

                        for dy in range(2, 6):
                            if not isfree(dy, rightcol, apos, bpos, cpos, dpos):
                                break
                            
                            if not hasbelow:
                                explore(pos, i, j, dy, rightcol, dy-1 + abs(rightcol-x))
                    else:
                        canmoveup = True

                        for dy in range(1, y):
                            if not isfree(dy, x, apos, bpos, cpos, dpos):
                                canmoveup = False
                                break

                        if not canmoveup:
                            continue

                        right = [dx for dx in range(x+1, 12)]
                        left = [dx for dx in range(x-1, 0, -1)]
                        
                        for direction in (right, left):
                            for dx in direction:
                                if not isfree(1, dx, apos, bpos, cpos, dpos):
                                    break

                                if dx not in otherrightcols:
                                    explore(pos, i, j, 1, dx, (y-1) + abs(dx-x))

        # blocker = False

        # for i, yx in enumerate(apos):
        #     y, x = yx
        #     if (y, x) in blocking:
        #         blocker = True
        #         for deltax in (-1, 1):
        #             if isfree(y, x+deltax, apos, bpos, cpos, dpos):
        #                 dapos = sorted(apos[:i] + [(y, x+deltax)] + apos[i+1:])
        #                 t = tuplify(dapos, bpos, cpos, dpos)
        #                 if t not in seen or seen[t] > energy+1:
        #                     seen[t] = energy+1
        #                     dh = heuristic(dapos, bpos, cpos, dpos)
        #                     heappush(states, [dh+energy+1, energy+1, dapos, list(bpos), list(cpos), list(dpos)])
        #         if x == 3 and isfree(2, 3, apos, bpos, cpos, dpos):
        #             containsothers = False
                    
        #             for pos in (bpos, cpos, dpos):
        #                 for dy, dx in pos:
        #                     if (dy, dx) in ((3, 3), (4, 3), (5, 3)):
        #                         containsothers = True
        #                         break

        #             if containsothers:
        #                 continue

        #             dapos = sorted(apos[:i] + [(2, 3)] + apos[i+1:])

        #             t = tuplify(dapos, bpos, cpos, dpos)
        #             if t not in seen or seen[t] > energy+1:
        #                 seen[t] = energy+1
        #                 dh = heuristic(dapos, bpos, cpos, dpos)
        #                 heappush(states, [dh+energy+1, energy+1, list(dapos), list(bpos), list(cpos), list(dpos)])
        # for i, yx in enumerate(bpos):
        #     y, x = yx
        #     if (y, x) in blocking:
        #         blocker = True
        #         for deltax in (-1, 1):
        #             if isfree(y, x+deltax, apos, bpos, cpos, dpos):
        #                 dbpos = sorted(bpos[:i] + [(y, x+deltax)] + bpos[i+1:])
        #                 t = tuplify(apos, dbpos, cpos, dpos)
        #                 if t not in seen or seen[t] > energy+10:
        #                     seen[t] = energy+10
        #                     dh = heuristic(apos, dbpos, cpos, dpos)
        #                     heappush(states, [dh+energy+10, energy+10, list(apos), dbpos, list(cpos), list(dpos)])
        #         if x == 5 and isfree(2, 5, apos, bpos, cpos, dpos):
        #             containsothers = False
                    
        #             for pos in (apos, cpos, dpos):
        #                 for dy, dx in pos:
        #                     if (dy, dx) in ((3, 5), (4, 5), (5, 5)):
        #                         containsothers = True
        #                         break

        #             if containsothers:
        #                 continue

        #             dbpos = sorted(bpos[:i] + [(2, 5)] + bpos[i+1:])

        #             t = tuplify(apos, dbpos, cpos, dpos)
        #             if t not in seen or seen[t] > energy+10:
        #                 seen[t] = energy+10
        #                 dh = heuristic(apos, dbpos, cpos, dpos)
        #                 heappush(states, [dh+energy+10, energy+10, list(apos), list(dbpos), list(cpos), list(dpos)])
        # for i, yx in enumerate(cpos):
        #     y, x = yx
        #     if (y, x) in blocking:
        #         blocker = True
        #         for deltax in (-1, 1):
        #             if isfree(y, x+deltax, apos, bpos, cpos, dpos):
        #                 dcpos = sorted(cpos[:i] + [(y, x+deltax)] + cpos[i+1:])
        #                 t = tuplify(apos, bpos, dcpos, dpos)
        #                 if t not in seen or seen[t] > energy+100:
        #                     seen[t] = energy+100
        #                     dh = heuristic(apos, bpos, dcpos, dpos)
        #                     heappush(states, [dh+energy+100, energy+100, list(apos), list(bpos), dcpos, list(dpos)])
        #         if x == 7 and isfree(2, 7, apos, bpos, cpos, dpos):
        #             containsothers = False
                    
        #             for pos in (apos, bpos, dpos):
        #                 for dy, dx in pos:
        #                     if (dy, dx) in ((3, 7), (4, 7), (5, 7)):
        #                         containsothers = True
        #                         break

        #             if containsothers:
        #                 continue

        #             dcpos = sorted(cpos[:i] + [(2, 7)] + cpos[i+1:])
                    
        #             t = tuplify(apos, bpos, dcpos, dpos)
        #             if t not in seen or seen[t] > energy+100:
        #                 seen[t] = energy+100
        #                 dh = heuristic(apos, bpos, dcpos, dpos)
        #                 heappush(states, [dh+energy+100, energy+100, list(apos), list(bpos), list(dcpos), list(dpos)])
        # for i, yx in enumerate(dpos):
        #     y, x = yx
        #     if (y, x) in blocking:
        #         blocker = True
        #         for deltax in (-1, 1):
        #             if isfree(y, x+deltax, apos, bpos, cpos, dpos):
        #                 ddpos = sorted(dpos[:i] + [(y, x+deltax)] + dpos[i+1:])
        #                 t = tuplify(apos, bpos, cpos, ddpos)
        #                 if t not in seen or seen[t] > energy+1000:
        #                     seen[t] = energy+1000
        #                     dh = heuristic(apos, bpos, cpos, ddpos)
        #                     heappush(states, [dh+energy+1000, energy+1000, list(apos), list(bpos), list(cpos), ddpos])
        #         if x == 9 and isfree(2, 9, apos, bpos, cpos, dpos):
        #             containsothers = False
                    
        #             for pos in (apos, bpos, cpos):
        #                 for dy, dx in pos:
        #                     if (dy, dx) in ((3, 9), (4, 9), (5, 9)):
        #                         containsothers = True
        #                         break

        #             if containsothers:
        #                 continue

        #             ddpos = sorted(dpos[:i] + [(2, 9)] + dpos[i+1:])
                    
        #             t = tuplify(apos, bpos, cpos, ddpos)
        #             if t not in seen or seen[t] > energy+1000:
        #                 seen[t] = energy+1000
        #                 dh = heuristic(apos, bpos, cpos, ddpos)
        #                 heappush(states, [dh+energy+1000, energy+1000, list(apos), list(bpos), list(cpos), list(ddpos)])

        # if blocker:
        #     continue

        # if apos != goala:
        #     for i in range(len(apos)):
        #         for dy, dx in neighs(apos[i][0], apos[i][1]):
        #             if (dy, dx) not in open:
        #                 continue
        #             if any((dy, dx) in pos for pos in allpos):
        #                 continue
        #             belowhas = False
        #             for down in range(1, 4):
        #                 for pos in (apos, bpos, cpos):
        #                     if (dpos[i][0]+down, dx) in pos:
        #                         belowhas = True     
        #                         break            
        #             if dy < apos[i][0] and dx == 3 and not belowhas:
        #                 continue
        #             if dy > apos[i][0] and dy == 2 and (dx != 3 or belowhas):
        #                 continue
        #             dapos = sorted(apos[:i] + [(dy, dx)] + apos[i+1:])
        #             t = tuplify(dapos, bpos, cpos, dpos)
        #             if t not in seen or seen[t] > energy+1:
        #                 seen[t] = energy+1
        #                 dh = heuristic(dapos, bpos, cpos, dpos)
        #                 heappush(states, [dh+energy+1, energy+1, list(dapos), list(bpos), list(cpos), list(dpos)])
        # if bpos != goalb:
        #     for i in range(len(bpos)):
        #         for dy, dx in neighs(bpos[i][0], bpos[i][1]):
        #             if (dy, dx) not in open:
        #                 continue
        #             if any((dy, dx) in pos for pos in allpos):
        #                 continue
        #             belowhas = False
        #             for down in range(1, 4):
        #                 for pos in (apos, bpos, cpos):
        #                     if (dpos[i][0]+down, dx) in pos:
        #                         belowhas = True     
        #                         break            
        #             if dy < bpos[i][0] and dx == 5 and not belowhas:
        #                 continue
        #             if dy > bpos[i][0] and dy == 2 and (dx != 5 or belowhas):
        #                 continue
        #             dbpos = sorted(bpos[:i] + [(dy, dx)] + bpos[i+1:])
        #             t = tuplify(apos, dbpos, cpos, dpos)
        #             if t not in seen or seen[t] > energy+10:
        #                 seen[t] = energy+10
        #                 dh = heuristic(apos, dbpos, cpos, dpos)
        #                 heappush(states, [dh+energy+10, energy+10, list(apos), list(dbpos), list(cpos), list(dpos)])
        # if cpos != goalc:
        #     for i in range(len(cpos)):
        #         for dy, dx in neighs(cpos[i][0], cpos[i][1]):
        #             if (dy, dx) not in open:
        #                 continue
        #             if any((dy, dx) in pos for pos in allpos):
        #                 continue
        #             belowhas = False
        #             for down in range(1, 4):
        #                 for pos in (apos, bpos, cpos):
        #                     if (dpos[i][0]+down, dx) in pos:
        #                         belowhas = True     
        #                         break            
        #             if dy < cpos[i][0] and dx == 7 and not belowhas:
        #                 continue
        #             if dy > cpos[i][0] and dy == 2 and (dx != 7 or belowhas):
        #                 continue
        #             dcpos = sorted(cpos[:i] + [(dy, dx)] + cpos[i+1:])
        #             t = tuplify(apos, bpos, dcpos, dpos)
        #             if t not in seen or seen[t] > energy+100:
        #                 seen[t] = energy+100
        #                 dh = heuristic(apos, bpos, dcpos, dpos)
        #                 heappush(states, [dh+energy+100, energy+100, list(apos), list(bpos), list(dcpos), list(dpos)])
        # if dpos != goald:
        #     for i in range(len(dpos)):
        #         for dy, dx in neighs(dpos[i][0], dpos[i][1]):                    
        #             if (dy, dx) not in open:
        #                 continue
        #             if any((dy, dx) in pos for pos in allpos):
        #                 continue                   
        #             belowhas = False
        #             for down in range(1, 4):
        #                 for pos in (apos, bpos, cpos):
        #                     if (dpos[i][0]+down, dx) in pos:
        #                         belowhas = True     
        #                         break            
        #             if dy < dpos[i][0] and dx == 9 and not belowhas:
        #                 continue
        #             if dy > dpos[i][0] and dy == 2 and (dx != 9 or belowhas):
        #                 continue
        #             ddpos = sorted(dpos[:i] + [(dy, dx)] + dpos[i+1:])
        #             t = tuplify(apos, bpos, cpos, ddpos)
        #             if t not in seen or seen[t] > energy+1000:
        #                 seen[t] = energy+1000
        #                 dh = heuristic(apos, bpos, cpos, ddpos)
        #                 heappush(states, [dh+energy+1000, energy+1000, list(apos), list(bpos), list(cpos), list(ddpos)])


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

# 58535 too high

# 37247 1906 5015594