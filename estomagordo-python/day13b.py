from collections import Counter, defaultdict, deque
from functools import reduce
from heapq import heappop, heappush
from itertools import combinations, permutations, product
from helpers import columns, digits, distance, distance_sq, eight_neighs, eight_neighs_bounded, grouped_lines, ints, manhattan, multall, n_neighs, neighs, neighs_bounded


def solve(dots, folds):
    d = set()

    for x, y in dots:        
        d.add((x, y))

    for alongx, val in folds:
        toremove = set()
        toadd = set()

        for x, y in d:
            if (alongx and x > val) or (not alongx and y > val):
                toremove.add((x, y))
                if alongx:
                    toadd.add((val-(x-val), y))
                else:
                    toadd.add((x, val-(y-val)))

        d |= toadd
        d -= toremove

    lowx = 100
    hix = -100
    lowy = 100
    hiy = -100

    for x, y in d:
        lowx = min(lowx, x)
        hix = max(hix, x)
        lowy = min(lowy, y)
        hiy = max(hiy, y)

    for y in range(lowy, hiy+1):
        row = [' ' for _ in range(hix-lowx+1)]
        for x in range(lowx, hix+1):
            if (x, y) in d:
                row[x] = '#'
        print(row)
    print(d)
    return len(d), lowx, hix, lowy, hiy

def main():
    dots = []
    folds = []
    gonnafold = False

    with open('13.txt') as f:
        for line in f.readlines():
            if gonnafold:
                l = line.rstrip().split()
                m = l[2].split('=')
                folds.append((m[0] == 'x', int(m[1])))
            elif line.rstrip():
                dots.append(ints(line))
            else:
                gonnafold = True
            
    return solve(dots, folds)


if __name__ == '__main__':
    print(main())
