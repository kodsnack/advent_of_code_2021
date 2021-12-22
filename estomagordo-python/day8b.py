from collections import Counter, defaultdict, deque
from functools import reduce
from heapq import heappop, heappush
from itertools import combinations, permutations, product
from helpers import distance, distance_sq, eight_neighs, eight_neighs_bounded, grouped_lines, ints, manhattan, multall, n_neighs, neighs, neighs_bounded, columns


def group_by_segment(display):
    bysegment = defaultdict(list)

    for val in display:        
        l = len(val)

        if l == 1:
            break

        bysegment[l].append(val)

    return bysegment


def build_key(bysegment, letters):
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

    return key


def build_canonical(val, key, letters):
    lets = []

    for c in val:
        for i, d in enumerate(key):
            if c == d:
                lets.append(letters[i])

    return ''.join(sorted(lets))


def build_translation(display, key, letters):
    translation = {}

    for val in display[:10]:
        l = len(val)
        s = build_canonical(val, key, letters)

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

    return translation


def calculate_value(display, key, letters, translation):
    weight = 1000
    total = 0

    for val in display[-4:]:
        s = build_canonical(val, key, letters)

        total += weight * translation[s]
        weight //= 10

    return total


def solve_display(display):
    letters = 'abcdefg'
    bysegment = group_by_segment(display)
    key = build_key(bysegment, letters)
    translation = build_translation(display, key, letters)

    return calculate_value(display, key, letters, translation)

def solve(lines):
    return sum(solve_display(line) for line in lines)

def main():
    lines = []

    with open('8.txt') as f:
        for line in f.readlines():
            vals = line.split()            
            lines.append(vals)
            
    return solve(lines)


if __name__ == '__main__':
    print(main())
