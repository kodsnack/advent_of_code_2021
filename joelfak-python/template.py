#!/usr/bin/env python3

import helpfunctions as hf
import sys, pytest

@hf.timing
def part1(data):
    return 0

@hf.timing
def part2(data):
    return 0

## Unit tests ########################################################

@pytest.fixture
def input():
    return 0

def test_part1_a(input):
    assert part1(input) == 0

## Main ########################################################

if __name__ == '__main__':

    with open(sys.argv[1]) as f:
        input = [line.strip() for line in f.readlines()]

    print("Advent of code day X")
    print(f"Part1 result: {part1(input.copy())}")
    print(f"Part2 result: {part2(input.copy())}")
