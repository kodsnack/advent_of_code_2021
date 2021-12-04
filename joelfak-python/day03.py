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

def extract_oxygen_generator_rating(data: list):
    for idx in range(len(data[0])):
        num_ones = sum([1 for number in data if number[idx] == '1'])
        num_zeros = len(data) - num_ones
        filter_value = '1' if num_ones >= num_zeros else '0'
        data = [number for number in data if number[idx] == filter_value]
        if len(data) == 1:
            break
    return int(data[0], 2)

def extract_co2_scrubber_rating(data: list):
    for idx in range(len(data[0])):
        num_ones = sum([1 for number in data if number[idx] == '1'])
        num_zeros = len(data) - num_ones
        filter_value = '1' if num_ones < num_zeros else '0'
        data = [number for number in data if number[idx] == filter_value]
        if len(data) == 1:
            break
    return int(data[0], 2)

@hf.timing
def part2(data):
    data = list(data)
    return extract_oxygen_generator_rating(data) * extract_co2_scrubber_rating(data)

## Unit tests ########################################################

test_input = ["00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001", "00010", "01010"]
def test_part1():
    assert part1(test_input) == 198

def test_extract_oxygen_generator_rating():
    assert extract_oxygen_generator_rating(test_input) == 23

def test_extract_co2_scrubber_rating():
    assert extract_co2_scrubber_rating(test_input) == 10

def test_part2():
    assert part2(test_input) == 230


## Main ########################################################

if __name__ == '__main__':

    print("Advent of code day X")
    print("Part1 result: {}".format(part1(hf.readFile(sys.argv[1]))))
    print("Part2 result: {}".format(part2(hf.readFile(sys.argv[1]))))
