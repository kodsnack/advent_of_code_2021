#!/usr/bin/env python3

from __future__ import annotations
import helpfunctions as hf
import sys
from collections import namedtuple

Pos = namedtuple('Pos', ['row', 'col'])

class Board():
    def __init__(self, board: list[list[int]]):
        self.board = board
        self.winning_number = None

    def get_number_position(self, number: int) -> Pos:
        has_number = False
        for row_nr, row in enumerate(self.board):
            if number in row:
                col_nr = row.index(number)
                has_number = True
                break
        return Pos(row_nr, col_nr) if has_number else None
        
    def mark_number(self, number: int) -> bool:
        pos = self.get_number_position(number)
        if pos:
            before = self.board[pos.row][pos.col]
            self.board[pos.row][pos.col] = None
            # print(f'Board: {self.board}, number: {number}, changing pos[{pos.row}][{pos.col}] from {before} to {self.board[pos.row][pos.col]}')
        
        if self._is_winning_board():
            self.winning_number = number
            return True
        else:
            return False
    
    def _is_winning_board(self) -> bool:
        has_winning_row = any( all(num is None for num in row) for row in self.board)
        has_winning_col = any( all(num is None for num in col) for col in zip(*self.board))
        return has_winning_row or has_winning_col
    
    def calculate_score(self) -> int:
        sum_ = sum(sum(num for num in row if num is not None) for row in self.board)
        print(f'sum: {sum_}, winning number: {self.winning_number}, score: {sum_*self.winning_number}')
        return sum_ * self.winning_number if self.winning_number is not None else 0

    def __repr__(self):
        return repr(self.board)

@hf.timing
def part1(input_numbers: list[int], boards: list[Board]):
    for number in input_numbers:
        for board in boards:
            if board.mark_number(number):
                return board.calculate_score()

@hf.timing
def part2(data):
    return 0

## Unit tests ########################################################

def test_part1():
    inputs = [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]
    boards = [Board([[22, 13, 17, 11,  0],
                     [ 8,  2, 23,  4, 24],
                     [21,  9, 14, 16,  7],
                     [ 6, 10,  3, 18,  5],
                     [ 1, 12, 20, 15, 19]]),
              Board([[ 3, 15,  0,  2, 22],
                     [ 9, 18, 13, 17,  5],
                     [19,  8,  7, 25, 23],
                     [20, 11, 10, 24,  4],
                     [14, 21, 16, 12,  6]]),
              Board([[14, 21, 17, 24,  4],
                     [10, 16, 15,  9, 19],
                     [18,  8, 23, 26, 20],
                     [22, 11, 13,  6,  5],
                     [ 2,  0, 12,  3,  7]])]
    assert part1(inputs, boards) == 4512

## Main ########################################################

def parse_data(filename):
    with open(filename) as f:
        numbers = list(map(int, f.readline().strip().split(',')))
        f.readline()
        boards = []
        board_matrix = []
        for line in (line.strip() for line in f.readlines()):
            if line != '':
                board_matrix.append(list(map(int, line.split())))
            else:
                boards.append(Board(board_matrix))
                board_matrix = []
    return numbers, boards
            

if __name__ == '__main__':

    print("Advent of code day X")
    print("Part1 result: {}".format(part1(*parse_data(sys.argv[1]))))
    # print("Part2 result: {}".format(part2(hf.getIntsFromFile(sys.argv[1]))))
