#!/usr/bin/env python3

import helpfunctions as hf
import sys, pytest

SPAWN_TIME = 6
INITIAL_SPAWN_TIME = 8

@hf.timing
def part1(state: list[int], days: int):
    print(state)
    for day in range(days):
        new_fishes = []
        for idx, n in enumerate(state):
            if n == 0:
                state[idx] = SPAWN_TIME
                new_fishes.append(INITIAL_SPAWN_TIME)
            else:
                state[idx] -= 1
        state.extend(new_fishes)
        # print(f'After {day+1} day: {state}')
    return len(state)

@hf.timing
def part2(data):
    return 0

## Unit tests ########################################################

@pytest.fixture
def input():
    return [3,4,3,1,2]

def test_part1_a(input):
    assert part1(input, 18) == 26

def test_part1_a(input):
    assert part1(input, 80) == 5934

## Main ########################################################

if __name__ == '__main__':

    with open(sys.argv[1]) as f:
        numbers = list(map(int, f.readline().strip().split(',')))

    print("Advent of code day 6")
    print("Part1 result: {}".format(part1(numbers, 80)))
    # print("Part2 result: {}".format(part2(hf.getIntsFromFile(sys.argv[1]))))
