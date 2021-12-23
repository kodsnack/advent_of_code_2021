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


def bfs(open, start):
    d = {}
    d[start] = []
    frontier = [[start]]

    for path in frontier:
        node = path[-1]
        y, x = node

        for dy, dx in neighs(y, x):
            if (dy, dx) in open and (dy, dx) not in d:
                d[(dy, dx)] = path + [(dy, dx)]
                frontier.append(path + [(dy, dx)])

    return d


def get_paths(open):    
    return {a: bfs(open, a) for a in open}


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
            if lines[y][x] not in ' #':
                open.add((y, x))

    paths = get_paths(open)    
    
    blocking = {(1, 3), (1, 5), (1, 7), (1, 9)}
    goala = [(2, 3), (3, 3), (4, 3), (5, 3)]
    goalb = [(2, 5), (3, 5), (4, 5), (5, 5)]
    goalc = [(2, 7), (3, 7), (4, 7), (5, 7)]
    goald = [(2, 9), (3, 9), (4, 9), (5, 9)]
    goals = [goala, goalb, goalc, goald]

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
        occupied = set(apos) | set(bpos) | set(cpos) | set(dpos)

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

        def cango(y1, x1, y2, x2):
            for dy, dx in paths[(y1, x1)][(y2, x2)][1:]:
                if (dy, dx) in occupied:
                    return False

            return True


        for i, pos in enumerate(allpos):
            rightcol = 3 + 2*i
            otherrightcols = {3 + 2*k for k in range(4)} - {rightcol}

            for j, yx in enumerate(pos):
                y, x = yx

                if y > 1:
                    cangoup = True
                    hasotherbelow = False
                    hasclearturn = isfree(1, x-1, apos, bpos, cpos, dpos) or isfree(1, x+1, apos, bpos, cpos, dpos)

                    if not hasclearturn:
                        continue

                    for gy in range(1, y):
                        if not isfree(gy, x, apos, bpos, cpos, dpos):
                            cangoup = False

                    if not cangoup:
                        continue
                    
                    for gy in range(y+1, 6):
                        for gpos in [allpos[k] for k in range(len(allpos)) if k != i]:
                            if (gy, x) in gpos:
                                hasotherbelow = True
                                break

                    if x == rightcol and not hasotherbelow:
                        continue
                            
                    for gy, gx in paths[(y, x)]:
                        if gx == x:
                            continue
                        if gy > 1:
                            continue

                        if cango(y, x, gy, gx):
                            explore(pos, i, j, gy, gx, len(paths[(y, x)][(gy, gx)]))
                else:
                    hasotheratgoal = False

                    for gy in range(2, 6):
                        for gpos in [allpos[k] for k in range(len(allpos)) if k != i]:
                            if (gy, rightcol) in gpos:
                                hasotheratgoal = True
                                break

                    if hasotheratgoal:
                        continue

                    for gy in range(5, 1, -1):
                        if cango(y, x, gy, rightcol):
                            explore(pos, i, j, gy, gx, len(paths[(y, x)][(gy, gx)]))

                # if x == rightcol:
                #     hasbelow = False
                #     for dy in range(y+1, 6):
                #         if hasbelow:
                #             break
                #         for posindex in range(4):
                #             if posindex == i:
                #                 continue
                #             if any(p == (dy, x) for p in allpos[posindex]):
                #                 hasbelow = True
                #                 break

                #     if not hasbelow:
                #         dy = y
                        
                #         while isfree(dy+1, x, apos, bpos, cpos, dpos) and dy < 5:
                #             dy += 1

                #         if dy > y:
                #             explore(pos, i, j, dy, x, distances[(y, x)][(dy, x)])

                #         continue

                #     canmoveup = True

                #     for dy in range(1, y):
                #         if not isfree(dy, x, apos, bpos, cpos, dpos):
                #             canmoveup = False
                #             break

                #     if not isfree(1, x-1, apos, bpos, cpos, dpos) and not isfree(1, x+1, apos, bpos, cpos, dpos):
                #         canmoveup = False

                #     if not canmoveup:
                #         continue

                #     right = [dx for dx in range(x+1, 12)]
                #     left = [dx for dx in range(x-1, 0, -1)]
                    
                #     for direction in (right, left):
                #         for dx in direction:
                #             if not isfree(1, dx, apos, bpos, cpos, dpos):
                #                 break

                #             if dx not in otherrightcols:
                #                 explore(pos, i, j, 1, dx, distances[(y, x)][(1, dx)])
                # else:
                #     hasbelow = False
                    
                #     for dy in range(2, 6):
                #         if hasbelow:
                #             break
                #         for posindex in range(4):
                #             if posindex == i:
                #                 continue
                #             if any(p == (dy, rightcol) for p in allpos[posindex]):
                #                 hasbelow = True
                #                 break

                #     if y == 1:
                #         direction = [dx for dx in range(x+1, rightcol+1)] if x < rightcol else [dx for dx in range(x-1, rightcol-1, -1)]
                #         valid = True

                #         for dx in direction:
                #             if not isfree(y, dx, apos, bpos, cpos, dpos):
                #                 valid = False
                #                 break

                #         if not valid:
                #             continue

                #         for dy in range(2, 6):
                #             if not isfree(dy, rightcol, apos, bpos, cpos, dpos):
                #                 break
                            
                #             if not hasbelow:
                #                 explore(pos, i, j, dy, rightcol, distances[(y, x)][(dy, rightcol)])
                #     else:
                #         canmoveup = True

                #         for dy in range(1, y):
                #             if not isfree(dy, x, apos, bpos, cpos, dpos):
                #                 canmoveup = False
                #                 break

                #         if not canmoveup:
                #             continue

                #         right = [dx for dx in range(x+1, 12)]
                #         left = [dx for dx in range(x-1, 0, -1)]
                        
                #         for direction in (right, left):
                #             for dx in direction:
                #                 if not isfree(1, dx, apos, bpos, cpos, dpos):
                #                     break

                #                 if dx not in otherrightcols:
                #                     explore(pos, i, j, 1, dx, distances[(y, x)][(1, dx)])


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