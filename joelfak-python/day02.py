#!/usr/bin/env python3

import helpfunctions as hf
import sys

@hf.timing
def part1(programmed_course: list[str]):
    depth = 0
    x = 0

    for command in programmed_course:
        direction, distance = command.split()
        distance = int(distance)
        if direction == 'forward':
            x += distance
        if direction == 'down':
            depth += distance
        if direction == 'up':
            depth -= distance
    return x * depth

@hf.timing
def part2(programmed_course: list[str]):
    depth = 0
    x = 0
    aim = 0

    for command in programmed_course:
        direction, distance = command.split()
        distance = int(distance)
        if direction == 'forward':
            x += distance
            depth += aim * distance
        if direction == 'down':
            aim += distance
        if direction == 'up':
            aim -= distance
    return x * depth

## Unit tests ########################################################

def test_part1():
    assert part1(['forward 5', 'down 5', 'forward 8', 'up 3', 'down 8', 'forward 2']) == 150

def test_part2():
    assert part2(['forward 5', 'down 5', 'forward 8', 'up 3', 'down 8', 'forward 2']) == 900

## Main ########################################################

if __name__ == '__main__':

    print("Advent of code day X")
    print("Part1 result: {}".format(part1(hf.readFile(sys.argv[1]))))
    print("Part2 result: {}".format(part2(hf.readFile(sys.argv[1]))))
