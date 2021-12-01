#!/usr/bin/env python3

from typing import Generator
import helpfunctions as hf
import sys

@hf.timing
def part1(input: Generator):
    input = list(input)
    return sum(1 for (a,b) in zip(input, input[1:]) if b>a)

@hf.timing
def part2(data):
    return 0

## Unit tests ########################################################

def test_part1():
    assert part1([199, 200, 208, 210, 200, 207, 240, 269, 260, 263]) == 7

## Main ########################################################

if __name__ == '__main__':

    print("Advent of code day 1")        
    print("Part1 result: {}".format(part1(hf.getIntsFromFile(sys.argv[1]))))
    print("Part2 result: {}".format(part2(hf.getIntsFromFile(sys.argv[1]))))
