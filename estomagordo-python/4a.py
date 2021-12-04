from collections import Counter, defaultdict, deque
from functools import reduce
from heapq import heappop, heappush
from itertools import combinations, permutations, product
from helpers import distance, distance_sq, eight_neighs, eight_neighs_bounded, grouped_lines, ints, manhattan, multall, n_neighs, neighs, neighs_bounded


def solve(calls, boards):
    for i in range(5, len(calls)+1):
        drawn = set(calls[:i])

        for board in boards:
            won = False
            
            for row in board:
                if all(num in drawn for num in row):
                    won = True
                    break

            for x in range(len(board[0])):
                if all(line[x] in drawn for line in board):
                    won = True
                    break

            if won:
                nonwon = 0
                
                for line in board:
                    for num in line:
                        if num not in drawn:
                            nonwon += int(num)

                return nonwon * int(calls[i-1])


if __name__ == '__main__':
    calls = []
    boards = []
    board = []

    with open('4.txt') as f:
        for line in f.readlines():
            if not calls:
                calls = line.split(',')
                continue
            if not line.strip():
                if board:
                    boards.append(board)
                    board = []
            else:
                board.append(line.split())
        boards.append(board)
            
    print(solve(calls, boards))
