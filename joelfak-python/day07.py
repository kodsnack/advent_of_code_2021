#!/usr/bin/env python3

import helpfunctions as hf
import sys, pytest
import numpy as np

@hf.timing
def part1(data):
    input = np.array(data)
    pos_range = range(min(data), max(data)+1)
    costs = {r:0 for r in pos_range}
    for pos in costs:
        costs[pos] = sum(abs(input-pos))
    return min(costs.values())

@hf.timing
def part2(data):
    input = np.array(data)
    pos_range = range(min(data), max(data)+1)
    costs = {r:0 for r in pos_range}
    for pos in costs:
        diff = abs(input-pos)
        costs[pos] = int(sum(diff*(diff+1)/2))
    return min(costs.values())

## Unit tests ########################################################

@pytest.fixture
def input():
    return [16,1,2,0,4,2,7,1,2,14]

def test_part1(input):
    assert part1(input) == 37

def test_part2(input):
    assert part2(input) == 168

## Main ########################################################

if __name__ == '__main__':

    with open(sys.argv[1]) as f:
        input = list(map(int, f.readline().strip().split(',')))

    print("Advent of code day 7")
    print(f"Part1 result: {part1(input.copy())}")
    print(f"Part2 result: {part2(input.copy())}")