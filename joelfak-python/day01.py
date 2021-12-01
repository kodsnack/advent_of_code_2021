#!/usr/bin/env python3

from typing import Generator
import helpfunctions as hf
import sys

@hf.timing
def part1(input: Generator[str, None, None]):
    input = list(input)
    return sum(1 for (a,b) in zip(input, input[1:]) if b>a)

@hf.timing
def part2(input: Generator[str, None, None]):
    input = list(input)
    return part1(map(sum, zip(input, input[1:], input[2:])))

## Unit tests ########################################################

def test_part1():
    assert part1(a for a in [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]) == 7

def test_part2():
    assert part2(a for a in [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]) == 5

## Main ########################################################

if __name__ == '__main__':

    print("Advent of code day 1")        
    print("Part1 result: {}".format(part1(hf.getIntsFromFile(sys.argv[1]))))
    print("Part2 result: {}".format(part2(hf.getIntsFromFile(sys.argv[1]))))
