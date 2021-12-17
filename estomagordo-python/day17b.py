from collections import Counter, defaultdict, deque
from functools import reduce
from heapq import heappop, heappush
from itertools import combinations, permutations, product
from helpers import chunks, chunks_with_overlap, columns, digits, distance, distance_sq, eight_neighs, eight_neighs_bounded, grouped_lines, ints, manhattan, multall, n_neighs, neighs, neighs_bounded


def solve(x1, x2, y1, y2):    
    steps = 57000
    limit = 56000
    count = 0

    for dx in range(1, 390):
        for dy in range(-320, 510):
            x = 0
            y = 0
            xvel = dx
            yvel = dy
            success = False

            for _ in range(steps):
                if abs(x)+abs(y) > limit:
                    break

                x += xvel
                y += yvel
                
                if xvel > 0:
                    xvel -= 1
                elif xvel > 0:
                    xvel += 1

                yvel -= 1

                if x1 <= x <= x2 and y1 <= y <= y2:
                    success = True

            if success:
                count += 1                
                print(dx, dy, count)

    return count



def main():
    with open('17.txt') as f:
        for line in f.readlines():
            x1, x2, y1, y2 = ints(line)
            return solve(x1, x2, y1, y2)

if __name__ == '__main__':
    print(main())