#!/usr/bin/env python3

import helpfunctions as hf
import sys, pytest
import numpy as np

def is_low_point(row_idx, col_idx, data):
    value = data[row_idx][col_idx]
    if row_idx-1 >= 0:
        if data[row_idx-1][col_idx] <= value:
            return False
    if row_idx+1 < len(data):
        if data[row_idx+1][col_idx] <= value:
            return False
    if col_idx-1 >= 0:
        if data[row_idx][col_idx-1] <= value:
            return False
    if col_idx+1 < len(data[0]):
        if data[row_idx][col_idx+1] <= value:
            return False
    return True

@hf.timing
def part1(data):
    summed_risk_levels = 0
    for row_idx, row in enumerate(data):
        for col_idx, value in enumerate(row):
            if is_low_point(row_idx, col_idx, data):
                summed_risk_levels += int(value) + 1
            else: print()
    return summed_risk_levels

def join_sets(classSets, class_a, class_b):
    joinedSet = set.union(classSets[class_a], classSets[class_b])
    for cl in joinedSet:
        classSets[cl] = joinedSet

@hf.timing
def part2(data):
    floodMap = np.zeros((len(data), len(data[0])), dtype=np.int16)
    currentClass = 0
    maxClass = 0
    classSizes = {}
    classSets = {}

    for row_idx, row in enumerate(data):
        for col_idx, value in enumerate(row):
            if value == '9':
                currentClass = -1
                floodMap[row_idx][col_idx] = -1
            else:
                classAbove = floodMap[row_idx-1][col_idx] if row_idx > 0 else -1
                classLeft = floodMap[row_idx][col_idx-1] if col_idx > 0 else -1
                if classAbove != classLeft and classAbove != -1 and classLeft != -1:
                    join_sets(classSets, classLeft, classAbove)
                if classAbove != -1:
                    currentClass = classAbove
                elif classLeft != -1:
                    currentClass = classLeft
                else:
                    maxClass += 1
                    currentClass = maxClass
                    classSets[currentClass] = {currentClass}

                floodMap[row_idx][col_idx] = currentClass
                classSizes[currentClass] = classSizes.get(currentClass, 0) + 1

    
    # print(classSets)
    # print(floodMap)

    basins = []
    basinSizes = []
    for key, basin in classSets.items():
        if basin not in basins:
            basins.append(basin)
            basinSizes.append(sum(classSizes[cl] for cl in basin))

    return np.prod(sorted(basinSizes, reverse=True)[0:3])

## Unit tests ########################################################

@pytest.fixture
def input():
    return ['2199943210',
            '3987894921',
            '9856789892',
            '8767896789',
            '9899965678']

def test_part1(input):
    assert part1(input) == 15

# def test_find_basins(input):

def test_part2(input):
    assert part2(input) == 1134


## Main ########################################################

if __name__ == '__main__':

    with open(sys.argv[1]) as f:
        input = [line.strip() for line in f.readlines()]

    print("Advent of code day 9")
    print(f"Part1 result: {part1(input.copy())}")
    print(f"Part2 result: {part2(input.copy())}")
