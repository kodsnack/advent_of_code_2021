#!/usr/bin/env python3

import helpfunctions as hf
import sys, pytest
# from collections import defaultdict

SPAWN_TIME = 6
INITIAL_SPAWN_TIME = 8

@hf.timing
def part1(state: list[int], days: int):
    # print(state)
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
def part2(inital_state: list[int], days: int):
    state = {key:0 for key in range(INITIAL_SPAWN_TIME+1)}

    for fish in inital_state:
        state[fish] = state[fish] + 1
    # print(state)

    for day in range(days):
        new_fishes = state[0]
        for key in range(1, INITIAL_SPAWN_TIME+1):
            state[key-1] = state[key]
        state[SPAWN_TIME] += new_fishes
        state[INITIAL_SPAWN_TIME] = new_fishes
        # print(f'After {day+1} day: {state.values()}')
    return sum(state.values())

## Unit tests ########################################################

@pytest.fixture
def input():
    return [3,4,3,1,2]

def test_part1_a(input):
    assert part1(input, 18) == 26

def test_part1_b(input):
    assert part1(input, 80) == 5934

def test_part2_a(input):
    assert part2(input, 18) == 26

def test_part2_b(input):
    assert part2(input, 80) == 5934

## Main ########################################################

if __name__ == '__main__':

    with open(sys.argv[1]) as f:
        numbers = list(map(int, f.readline().strip().split(',')))

    print("Advent of code day 6")
    print("Part1 result: {}".format(part1(numbers.copy(), 80)))
    print("Part2 result: {}".format(part2(numbers.copy(), 256)))
