from collections import Counter, defaultdict, deque
from functools import reduce
from heapq import heappop, heappush
from itertools import combinations, permutations, product
from re import S
from helpers import chunks, chunks_with_overlap, columns, digits, distance, distance_sq, eight_neighs, eight_neighs_bounded, grouped_lines, ints, manhattan, multall, n_neighs, neighs, neighs_bounded


def intersection(a, b):
        loxa, hixa, loya, hiya, loza, hiza = a
        loxb, hixb, loyb, hiyb, lozb, hizb = b

        if loxa <= loxb and hixa >= hixb and loya <= loyb and hiya >= hiyb and loza <= lozb and hiza >= hizb:
            return (loxb, hixb, loyb, hiyb, lozb, hizb)
        
        if loxa >= loxb and hixa <= hixb and loya >= loyb and hiya <= hiyb and loza >= lozb and hiza <= hizb:
            return (loxa, hixa, loya, hiya, loza, hiza)

        if loxa > hixb or loya > hiyb or loza > hizb or hixa < loxb or hiya < loyb or hiza < lozb:
            return (0, 0, 0, 0, 0, 0)

        return (max(loxa, loxb), min(hixa, hixb), max(loya, loyb), min(hiya, hiyb), max(loza, lozb), min(hiza, hizb))


def size(lox, hix, loy, hiy, loz, hiz):
    def d(n):
        return n
        return -50 if n < -50 else 50 if n > 50 else n
    return (d(hix)+1-d(lox))*(d(hiy)+1-d(loy))*(d(hiz)+1-d(loz))


def expand_steps(steps):
    newsteps = []

    for on, dims in steps:
        additional = []

        if on:
            additional.append((on, dims))

        for prevon, prevdims in newsteps:
            loxi, hixi, loyi, hiyi, lozi, hizi = intersection(dims, prevdims)

            if loxi == hixi:
                continue

            if on:
                if prevon:
                    additional.append((False, (loxi, hixi, loyi, hiyi, lozi, hizi)))
                else:
                    additional.append((True, (loxi, hixi, loyi, hiyi, lozi, hizi)))

            if not on:
                if prevon:
                    additional.append((False, (loxi, hixi, loyi, hiyi, lozi, hizi)))
                else:
                    additional.append((True, (loxi, hixi, loyi, hiyi, lozi, hizi)))
        
        newsteps += additional

    return newsteps


def solve(steps):
    count = 0

    expanded = expand_steps(steps)

    for on, dims in expanded:
        lox, hix, loy, hiy, loz, hiz = dims
        s = size(lox, hix, loy, hiy, loz, hiz)        

        if on:
            count += s
        else:
            count -= s

    return count

    # for i, step in enumerate(steps):
    #     on, dims = step
    #     lox, hix, loy, hiy, loz, hiz = dims
        
    #     if on:
    #         count += size(lox, hix, loy, hiy, loz, hiz)

    #         for j in range(i):
    #             onb, dimsb = steps[j]

    #             if not onb:
    #                 continue

    #             loxb, hixb, loyb, hiyb, lozb, hizb = dimsb
    #             loxo, hixo, loyo, hiyo, lozo, hizo = intersection(dims, dimsb)
    #             count -= size(loxo, hixo, loyo, hiyo, lozo, hizo)
    #     else:




        

    



def main():
    steps = []

    with open('22.txt') as f:
        for line in f.readlines():
            on = line[:2] == 'on'
            nums = ints(line)
            steps.append((on, nums))
            
    return solve(steps)


if __name__ == '__main__':
    print(main())

# 2758514936282235 example correct
# 1345283857688714 my example
# 1345188828823698 my new example