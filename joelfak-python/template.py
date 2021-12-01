#!/usr/bin/env python3

import helpfunctions as hf
import sys

@hf.timing
def part1(data):
    return 0

@hf.timing
def part2(data):
    return 0

## Unit tests ########################################################

def test_part1():
    assert part1(1) == 0

## Main ########################################################

if __name__ == '__main__':

    print("Advent of code day X")
    print("Part1 result: {}".format(part1(hf.getIntsFromFile(sys.argv[1]))))
    print("Part2 result: {}".format(part2(hf.getIntsFromFile(sys.argv[1]))))
