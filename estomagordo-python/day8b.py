from collections import Counter, defaultdict, deque
from functools import reduce
from heapq import heappop, heappush
from itertools import combinations, permutations, product
from helpers import distance, distance_sq, eight_neighs, eight_neighs_bounded, grouped_lines, ints, manhattan, multall, n_neighs, neighs, neighs_bounded, columns


def solve_display(display):
    letters = 'abcdefg'
    bysegment = defaultdict(list)

    for val in display:        
        l = len(val)

        if l == 1:
            break

        bysegment[l].append(val)

    key = [' ' for _ in range(7)]

    for letter in bysegment[3][0]:
        if letter not in bysegment[2][0]:
            key[0] = letter

    for letter in bysegment[4][0]:
        if letter not in bysegment[2][0] and all(letter in number for number in bysegment[6]):
            key[1] = letter

    for letter in bysegment[4][0]:
        if letter == key[1] or letter in bysegment[2][0]:
            continue

        key[3] = letter

    for dig in bysegment[6]:
        missing = [letter for letter in letters if letter not in dig][0]
        if missing in bysegment[2][0]:
            key[2] = missing

    counter = Counter()
    for dig in bysegment[5]:
        missing = [letter for letter in letters if letter not in dig]
        for letter in missing:
            counter[letter] += 1

    for k in counter.keys():
        if counter[k] == 1 and k not in key:
            key[5] = k
        if counter[k] == 2 and k not in key:
            key[4] = k

    for letter in letters:
        if letter not in key:
            key[6] = letter
    
    letter_table = {}

    for i, c in enumerate(bysegment[7][0]):
        letter_table[c] = letters[i]

    translation = {}

    for val in display[:10]:
        l = len(val)
        # lets = [letter_table[c] for c in val]
        lets = []
        for c in val:
            for i, d in enumerate(key):
                if c == d:
                    lets.append(letters[i])

        s = ''.join(sorted(lets))

        if l == 2:
            translation[s] = 1
        elif l == 3:
            translation[s] = 7
        elif l == 4:
            translation[s] = 4
        elif l == 7:
            translation[s] = 8
        else:
            if s == 'abcefg':
                translation[s] = 0
            if s == 'acdeg':
                translation[s] = 2
            if s == 'acdfg':
                translation[s] = 3
            if s == 'abdfg':
                translation[s] = 5
            if s == 'abdefg':
                translation[s] = 6
            if s == 'abcdfg':
                translation[s] = 9

    weight = 1000
    total = 0

    for val in display[-4:]:
        lets = []
        for c in val:
            for i, d in enumerate(key):
                if c == d:
                    lets.append(letters[i])

        s = ''.join(sorted(lets))

        total += weight * translation[s]
        weight //= 10

    return total


    # translation = {}
    # for i, c in enumerate(bysegment[7][0]):
    #     translation[c] = key[i]

    # for val in display[-4:]:
    #     s = ''        

    #     for c in val:
    #         s += translation[c]

    #     a = 22

    # letters = 'abcdefg'

    # mapping = {let: set('abcdefg') for let in letters}

    # for val in display:
    #     l = len(val)

    #     if l == 1:
    #         continue

    #     if l == 2:
    #         for letter in letters:
    #             if letter not in val:
    #                 mapping[letter].discard('c')
    #                 mapping[letter].discard('f')

    #     if l == 3:
    #         for letter in letters:
    #             if letter not in val:
    #                 mapping[letter].discard('a')
    #                 mapping[letter].discard('c')
    #                 mapping[letter].discard('f')

    #     if l == 4:
    #         for letter in letters:
    #             if letter not in val:
    #                 mapping[letter].discard('b')
    #                 mapping[letter].discard('c')
    #                 mapping[letter].discard('d')
    #                 mapping[letter].discard('f')

    # a = 22
    count = 0
    for p in permutations('abcdefg'):
        valid = True

        for val in display:
            l = len(val)

            if l == 2:
                for c in val:
                    if c not in (p[2], p[5]):
                        valid = False
            if l == 3:
                for c in val:
                    if c not in (p[0], p[2], p[5]):
                        valid = False
            if l == 4:
                for c in val:
                    if c not in (p[1], p[2], p[3], p[5]):
                        valid = False

            if l == 5:
                if val[0] != p[0] or val[2] != p[3] or val[-1] != p[-1]:
                    valid = False
            
        if not valid:
            continue

        count += 1
        continue

    return count
        
        # seen = False
        # digs = ''

        # for val in display:
        #     if val == '|':
        #         seen = True
        #     elif seen:
        #         l = len(val)

        #         if l == 2:
        #             digs += '1'
        #         elif l == 3:
        #             digs += '7'
        #         elif l == 4:
        #             digs += '4'
        #         elif l == 7:
        #             digs += '8'
        #         elif l == 5:
        #             if p[2] in val and p[5] in val:
        #                 digs += '3'
        #             elif p[2] in val:
        #                 digs += '2'
        #             else:
        #                 digs += '5'
        #         else:
        #             if p[3] in val:
        #                 if p[2] in val:
        #                     digs += '9'
        #                 else:
        #                     digs += '6'
        #             else:
        #                 digs += '0'

        # return int(''.join(digs))

def solve(lines):
    count = 0

    for line in lines:
        # if not any(len(s)==7 for s in line):
        #     count += 1
        count += solve_display(line)

    return count

    for p in permutations('abcdefg'):
        valid = False
        mapping = defaultdict(set)

        for line in lines:
            for val in line:
                if val == '|':
                    continue

            l = len(val)

            # if l == 2:
            #     if p[2] != val[0]:
            #         valid = False
            #     if p[5] != val[1]:
            #         valid = False
            # if l == 3:
            #     if p[0] != val[0]:
            #         valid = False
            #     if p[2] != val[1]:
            #         valid = False
            #     if p[5] != val[2]:
            #         valid = False
            if l == 7:
                if ''.join(p) != val:
                    valid = True

        if not valid:
            continue

        count = 0

        for line in lines:
            seen = False
            digs = ''

            for val in line:
                if val == '|':
                    seen = True
                elif seen:
                    l = len(val)

                    if l == 2:
                        digs += '1'
                    elif l == 3:
                        digs += '7'
                    elif l == 4:
                        digs += '4'
                    elif l == 7:
                        digs += '8'
                    elif l == 5:
                        if p[2] in val and p[5] in val:
                            digs += '3'
                        elif p[2] in val:
                            digs += '2'
                        else:
                            digs += '5'
                    else:
                        if p[3] in val:
                            if p[2] in val:
                                digs += '9'
                            else:
                                digs += '6'
                        else:
                            digs += '0'

            count += int(''.join(digs))

        return count

def main():
    lines = []

    with open('8.txt') as f:
        for line in f.readlines():
            vals = line.split()            
            lines.append(vals)
            
    return solve(lines)


if __name__ == '__main__':
    print(main())
