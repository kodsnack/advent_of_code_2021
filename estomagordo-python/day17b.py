from collections import Counter, defaultdict, deque
from functools import reduce
from heapq import heappop, heappush
from itertools import combinations, permutations, product
from helpers import chunks, chunks_with_overlap, columns, digits, distance, distance_sq, eight_neighs, eight_neighs_bounded, grouped_lines, ints, manhattan, multall, n_neighs, neighs, neighs_bounded


def solve(x1, x2, y1, y2):
    xmove = lambda dx, _: (-1, 0) if dx > 0 else (1, 0) if dx < 0 else (0, 0)
    xwin = lambda x, _: x >= x1
    xlose = lambda x, _, __, ___: x > x2

    ymove = lambda _, __: (0, -1)
    ywin = lambda _, y: y <= y2
    ylose = lambda _, __, y, dy: y < y1 and dy < 0
    
    def shoot(dx0, dy0, moves, wins, losses):
        x = 0
        y = 0
        dx = dx0
        dy = dy0

        while True:
            x += dx
            y += dy

            for move in moves:
                dx += move(dx, dy)[0]
                dy += move(dx, dy)[1]
        
            for loss in losses:
                if loss(x, dx, y, dy):
                    return False

            if all(win(x, y) for win in wins):
                return True

    def dxes():        
        mindx0 = int((2*x1)**0.5)
        maxdx0 = x2        

        return {dx0 for dx0 in range(mindx0, maxdx0+1) if shoot(dx0, 0, [xmove], [xwin], [xlose])}

    def dys():
        mindy0 = y1
        maxdy0 = 510 # pretty arbitrary

        return {dy0 for dy0 in range(mindy0, maxdy0+1) if shoot(0, dy0, [ymove], [ywin], [ylose])}    

    dxvals = dxes()
    dyvals = dys()

    return sum(shoot(dx, dy, [xmove, ymove], [xwin, ywin], [xlose, ylose]) for dx in dxvals for dy in dyvals)


def main():
    with open('17.txt') as f:
        for line in f.readlines():
            x1, x2, y1, y2 = ints(line)
            return solve(x1, x2, y1, y2)

if __name__ == '__main__':
    print(main())