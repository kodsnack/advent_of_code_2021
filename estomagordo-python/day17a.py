from collections import Counter, defaultdict, deque
from functools import reduce
from heapq import heappop, heappush
from itertools import combinations, permutations, product
from helpers import chunks, chunks_with_overlap, columns, digits, distance, distance_sq, eight_neighs, eight_neighs_bounded, grouped_lines, ints, manhattan, multall, n_neighs, neighs, neighs_bounded


def solve(x1, x2, y1, y2):
    highesty = -1000
    steps = 37000
    limit = 32000

    for dx in range(1, 260):
        for dy in range(210):
            x = 0
            y = 0
            xvel = dx
            yvel = dy
            thishighesty = y
            success = False

            for _ in range(steps):
                if abs(x)+abs(y) > limit:
                    break

                x += xvel
                y += yvel

                thishighesty = max(thishighesty, y)
                
                if xvel > 0:
                    xvel -= 1
                elif xvel > 0:
                    xvel += 1

                yvel -= 1

                if x > x2:
                    break

                if y < y1 and yvel < 0:
                    break

                if x1 <= x and y <= y2:
                    success = True
                    break

                if x == 0:
                    break

            if success:
                highesty = max(highesty, thishighesty)

    return highesty



def main():
    with open('17.txt') as f:
        for line in f.readlines():
            x1, x2, y1, y2 = ints(line)
            return solve(x1, x2, y1, y2)

if __name__ == '__main__':
    print(main())