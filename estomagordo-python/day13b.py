from collections import Counter, defaultdict, deque
from functools import reduce
from heapq import heappop, heappush
from itertools import combinations, permutations, product
from helpers import columns, digits, distance, distance_sq, eight_neighs, eight_neighs_bounded, grouped_lines, ints, manhattan, multall, n_neighs, neighs, neighs_bounded


def solve(dots, folds):
    dotset = set()

    for x, y in dots:        
        dotset.add((x, y))

    for alongx, val in folds:
        toremove = set()
        toadd = set()

        for x, y in dotset:
            if (alongx and x > val) or (not alongx and y > val):
                toremove.add((x, y))
                if alongx:
                    toadd.add((2*val-x, y))
                else:
                    toadd.add((x, 2*val-y))

        dotset |= toadd
        dotset -= toremove

    lox = min(point[0] for point in dotset)
    hix = max(point[0] for point in dotset)
    loy = min(point[1] for point in dotset)
    hiy = max(point[1] for point in dotset)

    image = []
    
    for y in range(loy, hiy+1):
        row = [' ' for _ in range(hix-lox+1)]

        for x in range(lox, hix+1):
            if (x, y) in dotset:
                row[x] = '#'
        
        image.append(row)

    return '\n'.join(''.join(row) for row in image)

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
