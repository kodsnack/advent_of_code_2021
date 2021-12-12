from collections import Counter, defaultdict, deque
from functools import reduce
from heapq import heappop, heappush
from itertools import combinations, permutations, product
from helpers import columns, digits, distance, distance_sq, eight_neighs, eight_neighs_bounded, grouped_lines, ints, manhattan, multall, n_neighs, neighs, neighs_bounded


def solve(lines):
    graph = defaultdict(list)

    translation = {}
    uppers = set()

    for a,b in lines:
        if a not in translation:
            translation[a] = len(translation)
        if b not in translation:
            translation[b] = len(translation)

        if a.isupper():
            uppers.add(translation[a])
        if b.isupper():
            uppers.add(translation[b])

        graph[translation[a]].append(translation[b])
        graph[translation[b]].append(translation[a])

    start = translation['start']
    end = translation['end']
    visited = Counter([start])
    
    def find(node):
        count = 0

        for following in graph[node]:
            if following == start:
                continue
            elif following == end:
                count += 1
            elif following in uppers:
                count += find(following)
            elif visited[following] < 1:
                visited[following] += 1
                count += find(following)
                visited[following] -= 1
            elif visited.most_common(1)[0][1] < 2:
                visited[following] += 1
                count += find(following)
                visited[following] -= 1

        return count

    return find(start)


def main():
    lines = []

    with open('12.txt') as f:
        for line in f.readlines():
            lines.append(line.rstrip().split('-'))
            
    return solve(lines)


if __name__ == '__main__':
    print(main())
