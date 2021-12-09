#!/usr/bin/env python3

import helpfunctions as hf
import sys, pytest

def is_low_point(row_idx, col_idx, data):
    value = data[row_idx][col_idx]
    if row_idx-1 >= 0:
        if data[row_idx-1][col_idx] <= value:
            return False
    if row_idx+1 < len(data):
        if data[row_idx+1][col_idx] <= value:
            return False
    if col_idx-1 >= 0:
        if data[row_idx][col_idx-1] <= value:
            return False
    if col_idx+1 < len(data[0]):
        if data[row_idx][col_idx+1] <= value:
            return False
    return True

@hf.timing
def part1(data):
    summed_risk_levels = 0
    for row_idx, row in enumerate(data):
        # print(row_idx)
        for col_idx, value in enumerate(row):
            print(row_idx, col_idx, value, end='')
            if is_low_point(row_idx, col_idx, data):
                print(' is low')
                summed_risk_levels += int(value) + 1
            else: print()
    return summed_risk_levels

@hf.timing
def part2(data):
    return 0

## Unit tests ########################################################

@pytest.fixture
def input():
    return ['2199943210',
            '3987894921',
            '9856789892',
            '8767896789',
            '9899965678']

def test_part1_a(input):
    assert part1(input) == 15

## Main ########################################################

if __name__ == '__main__':

    with open(sys.argv[1]) as f:
        input = [line.strip() for line in f.readlines()]

    print("Advent of code day X")
    print(f"Part1 result: {part1(input.copy())}")
    print(f"Part2 result: {part2(input.copy())}")
