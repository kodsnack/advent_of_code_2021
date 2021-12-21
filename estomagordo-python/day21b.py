from collections import Counter, defaultdict, deque
from functools import reduce
from heapq import heappop, heappush
from itertools import combinations, permutations, product
from helpers import chunks, chunks_with_overlap, columns, digits, distance, distance_sq, eight_neighs, eight_neighs_bounded, grouped_lines, ints, manhattan, multall, n_neighs, neighs, neighs_bounded


def solve(a, b):
    rolls = 0
    size = 10
    moves = 3
    dsize = 3
    rolls = Counter()
    seen = {}    

    for p in product(range(1,dsize+1), repeat=moves):
        rolls[sum(p)] += 1

    def count(a, b, ascore, bscore, arolling):
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
                outa, outb = count(newa, b, ascore+newa, bscore, False)
                awins += times * outa
                bwins += times * outb
        else:
            for score, times in rolls.items():
                newb = b + score
                if newb > size:
                    newb -= size
                outa, outb = count(a, newb, ascore, bscore+newb, True)
                awins += times * outa
                bwins += times * outb

        seen[tup] = (awins, bwins)

        return (awins, bwins)

    return max(count(a, b, 0, 0, True))


def main():
    players = []

    with open('21.txt') as f:
        for line in f.readlines():
            players.append(ints(line)[1])
            
    return solve(players[0], players[1])


if __name__ == '__main__':
    print(main())