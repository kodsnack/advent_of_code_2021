#!/usr/bin/env python3

from typing import Generator
import helpfunctions as hf
import sys
from pprint import pprint as pp

@hf.timing
def part1(data: Generator[str, None, None]):
    data_list = list(data)
    sums = []
    for idx in range(len(data_list[0])):
        sums.append(sum((int(num[idx]) for num in data_list)))

    alpha_rate_str = ""
    epsilon_rate_str = ""
    number_of_numbers = len(data_list)
    for n in sums:
        alpha_rate_str += '1' if n > number_of_numbers/2 else '0'
        epsilon_rate_str += '0' if n > number_of_numbers/2 else '1'
    
    alpha_rate = int(alpha_rate_str, 2)
    epsilon_rate = int(epsilon_rate_str, 2)
    return alpha_rate * epsilon_rate

@hf.timing
def part2(data):
    return 0

## Unit tests ########################################################

def test_part1():
    assert part1(["00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001", "00010", "01010", ]) == 198

## Main ########################################################

if __name__ == '__main__':

    print("Advent of code day X")
    print("Part1 result: {}".format(part1(hf.readFile(sys.argv[1]))))
    print("Part2 result: {}".format(part2(hf.getIntsFromFile(sys.argv[1]))))
