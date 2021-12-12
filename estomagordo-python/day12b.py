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
    visited = Counter()
    stack = [[start, 0]]
    count = 0

    while stack:
        node, index = stack.pop()                

        l = len(graph[node])

        if index == l:
            visited[node] -= 1
            continue

        following = graph[node][index]

        if following == end:
            count += 1
            stack.append([node, index+1])
            continue

        if following == start:
            stack.append([node, index+1])
            continue
        
        if following in uppers:
            stack.append([node, index+1])
            stack.append([following, 0])
        else:
            if following in visited and visited[following] > 0:
                if visited.most_common(1)[0][1] == 1:
                    stack.append([node, index+1])
                    stack.append([following, 0])
                    visited[following] += 1
                else:
                    stack.append([node, index+1])
            else:
                stack.append([node, index+1])
                stack.append([following, 0])
                visited[following] += 1

    return count


def main():
    lines = []

    with open('12.txt') as f:
        for line in f.readlines():
            lines.append(line.rstrip().split('-'))
            
    return solve(lines)


if __name__ == '__main__':
    print(main())
