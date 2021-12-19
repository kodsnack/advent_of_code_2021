from collections import Counter, defaultdict, deque
from functools import reduce
from heapq import heappop, heappush
from itertools import combinations, permutations, product
from helpers import chunks, chunks_with_overlap, columns, digits, distance, distance_sq, eight_neighs, eight_neighs_bounded, grouped_lines, ints, manhattan, multall, n_neighs, neighs, neighs_bounded

orientations = []
basic = [
    [[0, 1, 2], [1, 1, 1]],
    [[0, 1, 2], [-1, -1, 1]],
    [[1, 0, 2], [1, -1, 1]],
    [[1, 0, 2], [-1, 1, 1]],
    [[2, 1, 0], [1, 1, -1]],
    [[2, 1, 0], [-1, 1, 1]]
]
mods = [
    [-1, 1, 1],
    [-1, -1, -1],
    [1, 1, -1],
    [1, -1, 1]
]

for b, m in product(basic, mods):
    o, signs = b
    signs[1] *= m[1]
    signs[2] *= m[2]
    
    if m[0] == 1:
        o = [o[0], o[2], o[1]]
        signs = [signs[0], signs[2], signs[1]]

    orientations.append((tuple(o), tuple(signs)))

orientations = list(product(permutations(range(3)), product([1, -1], repeat=3)))

def locate(scannera, beaconsa, beaconsb, orientationa=[]):    
    ax, ay, az = scannera

    for colordera, inversionsa in (orientationa if orientationa else orientations):
        truebeacons = set()
        
        for beacona in beaconsa:
            truebeacona = [ax, ay, az]

            for pos in range(3):
                truebeacona[pos] += beacona[colordera[pos]] * inversionsa[colordera[pos]]

            truebeacons.add(tuple(truebeacona))

        for colorderb, inversionsb in orientations:
            potentialstarts = set()

            for tbax, tbay, tbaz in truebeacons:
                for beaconb in beaconsb:
                    potstartb = [tbax, tbay, tbaz]

                    for pos in range(3):
                        potstartb[pos] -= beaconb[colorderb[pos]] * inversionsb[colorderb[pos]]

                    potentialstarts.add(tuple(potstartb))

            for bx, by, bz in potentialstarts:
                matches = set()

                for beaconb in beaconsb:
                    truebeaconb = [bx, by, bz]

                    for pos in range(3):
                        truebeaconb[pos] += beaconb[colorderb[pos]] * inversionsb[colorderb[pos]]

                    if tuple(truebeaconb) in truebeacons:
                        matches.add(tuple(truebeaconb))
                        
                if len(matches) > 11:
                    return (True, [colordera, inversionsa], [colorderb, inversionsb], [bx, by, bz], matches)

    return (False, [], [], [], set())


def solve(scanners):
    n = len(scanners)
    locations = {0: (0, 0, 0)}
    orientationfor = {}
    
    while len(locations) < n:
        successinrun = False

        for i in range(n):
            if i not in locations:
                continue
            for j in range(n):
                if j in locations or i == j:
                    continue
                if i in orientationfor:
                    success, orientationsi, orientationsj, locationj, _ = locate(locations[i], scanners[i], scanners[j], [orientationfor[i]])
                    if success:
                        print(len(locations))
                        locations[j] = locationj
                        orientationfor[j] = orientationsj
                        successinrun = True
                        if i not in orientationfor:
                            orientationfor[i] = orientationsi
                else:
                    success, orientationsi, orientationsj, locationj, _ = locate(locations[i], scanners[i], scanners[j])
                    if success:
                        print(len(locations))
                        locations[j] = locationj
                        orientationfor[j] = orientationsj
                        successinrun = True
                        if i not in orientationfor:
                            orientationfor[i] = orientationsi

        if not successinrun:
            return
            
    longest = 0

    for i in range(n):
       for j in range(i+1,n):
           x1, y1, z1 = locations[i]
           x2, y2, z2 = locations[j]
           d = abs(x1-x2) + abs(y1-y2) + abs(z1-z2)

           longest = max(longest, d)

    return longest

def main():
    scanners = []
    scanner = []

    with open('19.txt') as f:
        for line in f.readlines():
            if not line.rstrip():
                scanners.append(scanner)
                continue

            nums = ints(line)

            if len(nums) == 1:
                scanner = []
            else:
                scanner.append(nums)

    scanners.append(scanner)

            
    return solve(scanners)


if __name__ == '__main__':
    print(main())
