from collections import Counter, defaultdict, deque
from functools import reduce
from heapq import heappop, heappush
from itertools import combinations, permutations, product
from helpers import chunks, chunks_with_overlap, columns, digits, distance, distance_sq, eight_neighs, eight_neighs_bounded, grouped_lines, ints, manhattan, multall, n_neighs, neighs, neighs_bounded


def solve(scanners):
    n = len(scanners)
    locations = {0: [0, 0, 0]}
    
    while len(locations) != n:
        for i in range(n-1):
            if i not in locations:
                continue

            scanneri = locations[i]
            for j in range(i+1, n):
                if j in locations:
                    continue

                proposals = Counter()

                for x1, y1, z1 in scanners[i]:
                    for x2, y2, z2 in scanners[j]:            
                        for p in permutations(range(3)):
                            for directionswaps in product([False, True], repeat=3):
                                detection = [x2, y2, z2]
                                values = [detection[p[0]], detection[p[1]], detection[p[2]]]
                                
                                for ii, b in enumerate(directionswaps):
                                    if b:
                                        values[ii] *= -1

                                scanner1 = (values[0]+x1, values[1]+y1, values[2]+z1)
                                proposals[scanner1] += 1

                coords, count = proposals.most_common(1)[0]

                if count == 12:
                    locations[j] = [scanneri[0]+coords[0], scanneri[1]+coords[1], scanneri[2]+coords[2]]

    return locations
                    


    # for p in permutations(range(3)):
    #     for directionswaps in product([False, True], repeat=3):
    #         overlaps = 0
            
    #         for detection in scanners[1]:
    #             values = [detection[p[0]], detection[p[1]], detection[p[2]]]
                # for i, b in enumerate(directionswaps):
                #     if b:
                #         values[i] *= -1

    #             if values in scanners[0]:
    #                 overlaps += 1

    #         print(overlaps)


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
