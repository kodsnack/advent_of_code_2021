from collections import Counter, defaultdict, deque
from functools import reduce
from heapq import heappop, heappush
from itertools import combinations, permutations, product
from helpers import chunks, chunks_with_overlap, columns, digits, distance, distance_sq, eight_neighs, eight_neighs_bounded, grouped_lines, ints, manhattan, multall, n_neighs, neighs, neighs_bounded


def solve(lines):
    a = 4
    b = 8

    d = 1
    dsize = 100
    rolls = 0
    scora = 0 
    scorb = 0
    arolling = True
    goal = 1000
    size = 10
    moves = 3
    rolls = Counter()
    seen = {}    

    for p in product(range(1,4), repeat=3):
        rolls[sum(p)] += 1

    def solve(a, b, ascore, bscore, arolling):
        if ascore > 20:
            return (1, 0)
        if bscore > 20:
            return (0, 1)

        tup = (a, b, ascore, bscore, arolling)

        if tup in seen:
            return seen[tup]

        awins = 0
        bwins = 0        
        
        if arolling:            
            for score, times in rolls.items():
                newa = a + score
                if newa > size:
                    newa -= size
                outa, outb = solve(newa, b, ascore+newa, bscore, False)
                awins += times * outa
                bwins += times * outb
        else:
            for score, times in rolls.items():
                newb = b + score
                if newb > size:
                    newb -= size
                outa, outb = solve(a, newb, ascore, bscore+newb, False)
                awins += times * outa
                bwins += times * outb

        seen[tup] = (awins, bwins)

        return (awins, bwins)

    return max(solve(a, b, 0, 0, True))

def main():
    lines = []

    with open('21.txt') as f:
        for line in f.readlines():
            lines.append(line)
            
    return solve(lines)


if __name__ == '__main__':
    print(main())
