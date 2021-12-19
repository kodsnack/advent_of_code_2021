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


def true_beacons(colorder, inversions, beacons, start):
    truebeacons = set()
        
    for beacon in beacons:
        truebeacon = list(start)

        for pos in range(3):
            truebeacon[pos] += beacon[colorder[pos]] * inversions[colorder[pos]]

        truebeacons.add(tuple(truebeacon))

    return truebeacons


def locate(scannera, beaconsa, beaconsb, orientationa=[]):
    for colordera, inversionsa in ([orientationa] if (orientationa and len(orientationa) == 2) else orientations):
        truebeacons = true_beacons(colordera, inversionsa, beaconsa, scannera)

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


def connect_scanners(scanners, n):
    locations = {0: (0, 0, 0)}
    orientationfor = defaultdict(list)
    
    while len(locations) < n:
        for i, j in [(i, j) for i in range(n) for j in range(n) if i in locations and j not in locations]:
            success, orientationsi, orientationsj, locationj, _ = locate(locations[i], scanners[i], scanners[j], orientationfor[i])
            if success:
                locations[j] = locationj
                orientationfor[i] = orientationsi
                orientationfor[j] = orientationsj             

    return locations, orientationfor


def solve(scanners):
    n = len(scanners)
    locations, orientationfor = connect_scanners(scanners, n)
    allbeacs = set()

    for i in range(n):
        for beacon in scanners[i]:
            colorder, inversions = orientationfor[i]
            truebeacon = list(locations[i])

            for pos in range(3):
                truebeacon[pos] += beacon[colorder[pos]] * inversions[colorder[pos]]

            allbeacs.add(tuple(truebeacon))

    return len(allbeacs)

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
