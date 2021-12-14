from collections import Counter, defaultdict, deque
from functools import reduce
from heapq import heappop, heappush
from itertools import combinations, permutations, product
from helpers import columns, digits, distance, distance_sq, eight_neighs, eight_neighs_bounded, grouped_lines, ints, manhattan, multall, n_neighs, neighs, neighs_bounded


def solve(chain, transforms, times=10):
    chain = 'PHVCVBFHCVPFKBNHKNBO'
    pairs = []

    for x in range(1, len(chain)):
        pairs.append(chain[x-1]+chain[x])

    seen = {}

    def helper(pair, remaining, letter):
        if remaining == 0:
            return pair.count(letter)
            for tp, _, middle in transforms:
                if tp == pair:
                    return (pair+middle).count(letter)

        if (pair, remaining, letter) in seen:
            return seen[(pair, remaining, letter)]

        count = 0

        for tp, _, middle in transforms:
            if tp == pair:
                count = helper(pair[0] + middle, remaining-1, letter) + helper(middle+pair[1], remaining-1, letter)#//(2 if remaining == 1 else 1)
                break

        seen[(pair, remaining, letter)] = count

        return count

    lettersums = []
    alletters = set(chain)
    # pairs = ['NC']
    for _, _, let in transforms:
        alletters.add(let)
    print(alletters)
    for letter in alletters:
        total = 0#-chain[1:-1].count(letter)
        for pair in pairs:
            v = helper(pair, times, letter)
            total += v - (v - pair.count(letter))//2
        lettersums.append(total)
        print(letter, total)

    lettersums.sort()
    print(lettersums)
    return lettersums[-1]-lettersums[0]

    for step in range(times):
        newchain = []

        for x in range(1, len(chain)):
            ab = chain[x-1]+chain[x]
            found = False

            for pair, _, middle in transforms:
                if pair == ab:
                    if x == 1:
                        newchain.append(ab[0] + middle + ab[1])
                    else:
                        newchain.append(middle + ab[1])                    
                    found = True
                    break
            
            if not found:
                newchain.append(ab)

        chain = ''.join(newchain)
        c = Counter(chain)
        n = len(c)
        print(step, c)

        print(step, c.most_common(1)[0][1], c.most_common(n)[-1][1], c.most_common(1)[0][1] - c.most_common(n)[-1][1])


    c = Counter(chain)
    n = len(c)

    return c.most_common(1)[0][1] - c.most_common(n)[-1][1]


def main():
    chain = 'PHVCVBFHCVPFKBNHKNBO'
    transforms = []

    with open('14.txt') as f:
        for line in f.readlines():
            transforms.append(line.split())
            
    return solve(chain, transforms)


if __name__ == '__main__':
    print(main())

# 4439442043737 too low