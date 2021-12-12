from collections import Counter, defaultdict, deque
from functools import reduce
from heapq import heappop, heappush
from itertools import combinations, permutations, product
from helpers import columns, digits, distance, distance_sq, eight_neighs, eight_neighs_bounded, grouped_lines, ints, manhattan, multall, n_neighs, neighs, neighs_bounded


def can_add(path, node):
    if node == 'start':
        return False

    if node.isupper():
        return True

    nodecounts = Counter(path)

    if node not in nodecounts:
        return True

    if nodecounts[node] == 2:
        return False

    return not any(k.islower() and nodecounts[k] == 2 for k in nodecounts.keys())


def solve(lines):
    graph = defaultdict(list)

    for a,b in lines:
        graph[a].append(b)
        graph[b].append(a)

    visited = Counter()
    stack = [['start', 0]]
    count = 0

    while stack:
        node, index = stack.pop()                

        l = len(graph[node])

        if index == l:
            visited[node] -= 1
            continue

        following = graph[node][index]

        if following == 'end':
            count += 1
            stack.append([node, index+1])
            continue

        if following == 'start':
            stack.append([node, index+1])
            continue
        
        if following.isupper():
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

    paths = set()
    frontier = [['start']]

    for path in frontier:
        if path[-1] == 'end':
            paths.add(tuple(path))
            continue

        for node in graph[path[-1]]:
            if not can_add(path, node):
                continue

            frontier.append(path + [node])

    return len(paths)


def main():
    lines = []

    with open('12.txt') as f:
        for line in f.readlines():
            lines.append(line.rstrip().split('-'))
            
    return solve(lines)


if __name__ == '__main__':
    print(main())
