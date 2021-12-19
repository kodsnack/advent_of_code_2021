from collections import Counter, defaultdict, deque
from functools import reduce
from heapq import heappop, heappush
from itertools import combinations, permutations, product
from helpers import chunks, chunks_with_overlap, columns, digits, distance, distance_sq, eight_neighs, eight_neighs_bounded, grouped_lines, ints, manhattan, multall, n_neighs, neighs, neighs_bounded

# orientations = list(product(permutations(range(3)), product([False, True], repeat=3)))
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
# print(orientations)
print(len(orientations), len(set(orientations)))

def locate(scannera, beaconsa, beaconsb, orientationa=[]):    
    ax, ay, az = scannera

    for colordera, inversionsa in (orientationa if orientationa else orientations):
        truebeacons = set()
        
        for beacona in beaconsa:
            truebeacona = [ax, ay, az]

            for pos in range(3):
                truebeacona[pos] += beacona[colordera[pos]] * inversionsa[colordera[pos]]
                # truebeacona[colordera[pos]] += beacona[colordera[pos]] * inversionsa[colordera[pos]]

            truebeacons.add(tuple(truebeacona))

        for colorderb, inversionsb in orientations:
            potentialstarts = set()

            for tbax, tbay, tbaz in truebeacons:
                for beaconb in beaconsb:
                    potstartb = [tbax, tbay, tbaz]

                    for pos in range(3):
                        potstartb[pos] -= beaconb[colorderb[pos]] * inversionsb[colorderb[pos]]
                        # potstartb[colorderb[pos]] -= beaconb[colorderb[pos]] * inversionsb[colorderb[pos]]

                    potentialstarts.add(tuple(potstartb))

            for bx, by, bz in potentialstarts:
                matches = 0

                for beaconb in beaconsb:
                    truebeaconb = [bx, by, bz]

                    for pos in range(3):
                        truebeaconb[pos] += beaconb[colorderb[pos]] * inversionsb[colorderb[pos]]
                        # truebeaconb[colorderb[pos]] += beaconb[colorderb[pos]] * inversionsb[colorderb[pos]]

                    if tuple(truebeaconb) in truebeacons:
                        matches += 1
                        
                if matches > 11:
                    print('match', len(potentialstarts))
                    return (True, [colordera, inversionsa], [colorderb, inversionsb], [bx, by, bz], matches)

    return (False, [], [], [], -1)


def solve(scanners):
    n = len(scanners)
    locations = {0: (0, 0, 0)}
    orientationfor = {}

    _, orientations0, orientations1, location1, __ = locate([0, 0, 0], scanners[0], scanners[1])

    locations[1] = location1
    orientationfor[0] = orientations0
    orientationfor[1] = orientations1
    
    while len(locations) < n:
        successinrun = False

        for i in range(n-1):
            if i not in locations:
                continue
            for j in range(i+1, n):
                if j in locations:
                    continue
                if i in orientationfor:
                    success, _, orientationsj, locationj, __ = locate(locations[i], scanners[i], scanners[j], [orientationfor[i]])
                    if success:
                        locations[j] = locationj
                        orientationfor[j] = orientationsj
                        successinrun = True
                        print(locations, orientationfor)
                else:
                    success, _, orientationsj, locationj, __ = locate(locations[i], scanners[i], scanners[j])
                    if success:
                        locations[j] = locationj
                        orientationfor[j] = orientationsj
                        successinrun = True
                        print(locations, orientationfor)

        if not successinrun:
            break

    return locations


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