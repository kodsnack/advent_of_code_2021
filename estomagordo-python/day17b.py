from collections import Counter, defaultdict, deque
from functools import reduce
from heapq import heappop, heappush
from itertools import combinations, permutations, product
from helpers import chunks, chunks_with_overlap, columns, digits, distance, distance_sq, eight_neighs, eight_neighs_bounded, grouped_lines, ints, manhattan, multall, n_neighs, neighs, neighs_bounded


def solve(x1, x2, y1, y2):    
    minx = int((2*x1)**0.5)
    count = 0

    for dx in range(minx, x2+1):
        for dy in range(y1, 510):
            x = 0
            y = 0
            xvel = dx
            yvel = dy
            success = False

            while True:
                x += xvel
                y += yvel
                
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
                count += 1

    return count



def main():
    with open('17.txt') as f:
        for line in f.readlines():
            x1, x2, y1, y2 = ints(line)
            return solve(x1, x2, y1, y2)

if __name__ == '__main__':
    print(main())