from collections import Counter, defaultdict, deque
from functools import reduce
from heapq import heappop, heappush
from itertools import combinations, permutations, product
from helpers import chunks, chunks_with_overlap, columns, digits, distance, distance_sq, eight_neighs, eight_neighs_bounded, grouped_lines, ints, manhattan, multall, n_neighs, neighs, neighs_bounded


def overlaps(scannera, truebeaconsa, beaconsa, beaconsb):
    best = [-1]

    for p in permutations(range(3)):
        for directionswaps in product([False, True], repeat=3):
            for i, beaconi in enumerate(beaconsa):
                for j, beaconj in enumerate(beaconsb):
                    scannerbproposx = beaconi[p[0]] - scannera[p[0]] + (-beaconj[p[0]] if directionswaps[p[0]] else beaconj[p[0]])
                    scannerbproposy = beaconi[p[1]] - scannera[p[1]] + (-beaconj[p[1]] if directionswaps[p[1]] else beaconj[p[1]])
                    scannerbproposz = beaconi[p[2]] - scannera[p[2]] + (-beaconj[p[2]] if directionswaps[p[2]] else beaconj[p[2]])

                    scannerbpropos = [scannerbproposx, scannerbproposy, scannerbproposz]

                    count = 0

                    for jj, beaconjj in enumerate(beaconsb):
                        truex = 

def solve(scanners):
    n = len(scanners)
    locations = {0: (0, 0, 0)}
    
    while len(locations) != n:
        for i in range(n-1):
            if i not in locations:
                continue

            scanneri = locations[i]
            for j in range(i+1, n):
                if j in locations:
                    continue

                for x1, y1, z1 in scanners[i]:
                    if j in locations:
                        break
                    for x2, y2, z2 in scanners[j]:        
                        if j in locations:
                            break    
                        for p in permutations(range(3)):
                            if j in locations:
                                break
                            for directionswaps in product([False, True], repeat=3):
                                if j in locations:
                                    break
                                detection = [x2, y2, z2]
                                values = [detection[p[0]], detection[p[1]], detection[p[2]]]
                                
                                for ii, b in enumerate(directionswaps):
                                    if b:
                                        values[ii] *= -1

                                scannerj = (values[0]+x1, values[1]+y1, values[2]+z1)
                                count = 0

                                for detectionj in scanners[j]:
                                    detectionix = scannerj[p[0]] - (detectionj[p[0]] * (-1 if directionswaps[p[0]] else 1))
                                    detectioniy = scannerj[p[1]] - (detectionj[p[1]] * (-1 if directionswaps[p[1]] else 1))
                                    detectioniz = scannerj[p[2]] - (detectionj[p[2]] * (-1 if directionswaps[p[2]] else 1))

                                    if [detectionix, detectioniy, detectioniz] in scanners[i]:
                                        count += 1

                                if count > 11:
                                    locations[j] = scannerj

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
