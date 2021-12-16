from collections import Counter, defaultdict, deque
from functools import reduce
from heapq import heappop, heappush
from itertools import combinations, permutations, product
from helpers import chunks, chunks_with_overlap, columns, digits, distance, distance_sq, eight_neighs, eight_neighs_bounded, grouped_lines, ints, manhattan, multall, n_neighs, neighs, neighs_bounded


def solve(chain, transforms, times=10):
    letters = Counter(chain)
    seen = {}

    def helper(pair, remaining):
        if remaining == 0:
            return Counter()

        if (pair, remaining) in seen:
            return seen[(pair, remaining)]

        for tp, _, middle in transforms:
            if tp == pair:
                result = Counter(middle) + helper(tp[0]+middle, remaining-1) + helper(middle+tp[1], remaining-1)
                seen[(pair, remaining)] = result
                return result

    for pair in chunks_with_overlap(chain, 2):
        letters += helper(pair, times)
    
    return max(letters.values()) - min(letters.values())


def main():
    chain = ''
    transforms = []

    with open('14.txt') as f:
        for line in f.readlines():
            if not chain:
                chain = line.rstrip()
            elif line.rstrip():
                transforms.append(line.split())
            
    return solve(chain, transforms)


if __name__ == '__main__':
    print(main())