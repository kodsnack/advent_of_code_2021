from collections import Counter, defaultdict, deque
from functools import reduce
from heapq import heappop, heappush
from itertools import combinations, permutations, product
from helpers import columns, digits, distance, distance_sq, eight_neighs, eight_neighs_bounded, grouped_lines, ints, manhattan, multall, n_neighs, neighs, neighs_bounded


def solve(lines):
    count = 0

    for line in lines:
        stack = []

        for c in line:
            if c in '([{<':
                stack.append(c)
            elif c == ')':
                if stack[-1] != '(':
                    count += 3
                    break
                stack.pop()
            elif c == ']':
                if stack[-1] != '[':
                    count += 57
                    break
                stack.pop()
            elif c == '}':
                if stack[-1] != '{':
                    count += 1197
                    break
                stack.pop()
            elif c == '>':
                if stack[-1] != '<':
                    count += 25137
                    break
                stack.pop()

    return count


def main():
    lines = []

    with open('10.txt') as f:
        for line in f.readlines():
            lines.append(line.rstrip())
            
    return solve(lines)


if __name__ == '__main__':
    print(main())
