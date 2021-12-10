from collections import Counter, defaultdict, deque
from functools import reduce
from heapq import heappop, heappush
from itertools import combinations, permutations, product
from helpers import columns, digits, distance, distance_sq, eight_neighs, eight_neighs_bounded, grouped_lines, ints, manhattan, multall, n_neighs, neighs, neighs_bounded


def solve(lines):
    scores = []

    for line in lines:
        stack = []
        corrupt = False

        for c in line:
            if c in '([{<':
                stack.append(c)
            elif c == ')':
                if not stack or stack[-1] != '(':
                    corrupt = True
                    break
                stack.pop()
            elif c == ']':
                if not stack or stack[-1] != '[':
                    corrupt = True
                    break
                stack.pop()
            elif c == '}':
                if not stack or stack[-1] != '{':
                    corrupt = True
                    break
                stack.pop()
            elif c == '>':
                if not stack or stack[-1] != '<':
                    corrupt = True
                    break
                stack.pop()

        points = 0

        if corrupt:
            continue

        for c in stack[::-1]:
            points *= 5
            points += (1 if c == '(' else 2 if c == '[' else 3 if c == '{' else 4)

        scores.append(points)

    scores.sort()
    l = len(scores)

    return scores[l//2]


def main():
    lines = []

    with open('10.txt') as f:
        for line in f.readlines():
            lines.append(line.rstrip())
            
    return solve(lines)


if __name__ == '__main__':
    print(main())
