from collections import Counter, defaultdict, deque
from functools import reduce
from heapq import heappop, heappush
from itertools import combinations, permutations, product
from helpers import columns, digits, distance, distance_sq, eight_neighs, eight_neighs_bounded, grouped_lines, ints, manhattan, multall, n_neighs, neighs, neighs_bounded


def corruption_score(line):
    stack = []

    for c in line:
        if c in '([{<':
            stack.append(c)
        elif c == ')':
            if stack[-1] != '(':
                return 3
            stack.pop()
        elif c == ']':
            if stack[-1] != '[':
                return 57
            stack.pop()
        elif c == '}':
            if stack[-1] != '{':
                return 1197
            stack.pop()
        elif c == '>':
            if stack[-1] != '<':
                return 25137
            stack.pop()

    return 0


def solve(lines):
    return sum(corruption_score(line) for line in lines)


def main():
    lines = []

    with open('10.txt') as f:
        for line in f.readlines():
            lines.append(line.rstrip())
            
    return solve(lines)


if __name__ == '__main__':
    print(main())
