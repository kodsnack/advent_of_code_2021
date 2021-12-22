from collections import Counter, defaultdict, deque
from functools import reduce
from heapq import heappop, heappush
from itertools import combinations, permutations, product
from helpers import columns, digits, distance, distance_sq, eight_neighs, eight_neighs_bounded, grouped_lines, ints, manhattan, multall, n_neighs, neighs, neighs_bounded


def solve(dots, folds):
    d = set()

    for x, y in dots:        
        d.add((x, y))

    for alongx, val in folds[:1]:
        toremove = set()
        toadd = set()

        for x, y in d:
            if (alongx and x > val) or (not alongx and y > val):
                toremove.add((x, y))
                if alongx:
                    toadd.add((2*val-x, y))
                else:
                    toadd.add((x, 2*val-y))

        d |= toadd
        d -= toremove

    return len(d)

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
