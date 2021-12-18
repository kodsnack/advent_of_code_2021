#!/usr/bin/env python3

import helpfunctions as hf
import sys, pytest
from collections import namedtuple

Coord = namedtuple('Coord', ['x', 'y'])


class VentMap():
    def __init__(self, input: list[tuple[Coord, Coord]], allow_diagonals=False):
        size = max(max(max(input))) + 1
        self.map = [[0] * size for i in range(size)]
        
        for (start, end) in input:
            x_step = 1 if end.x > start.x else -1
            y_step = 1 if end.y > start.y else -1
            if start.x == end.x:
                y_range = range(start.y, end.y+y_step, y_step)
                x_range = [start.x] * len(y_range)
            elif start.y == end.y:
                x_range = range(start.x, end.x+x_step, x_step)
                y_range = [start.y] * len(x_range)
            elif allow_diagonals and (abs(start.x-end.x) == abs(start.y-end.y)):
                x_range = range(start.x, end.x+x_step, x_step)
                y_range = range(start.y, end.y+y_step, y_step)
            else:
                continue

            for x, y in zip(x_range, y_range):
                self.map[y][x] += 1

    def get_map(self):
        return [''.join(map(str, row)).replace('0','.') for row in self.map]

    def get_intersections(self):
        return sum(sum(item > 1 for item in row) for row in self.map)
   
    def __repr__(self):
        return str(self.get_map())
        
    def __str__(self):
        return '\n'.join(self.get_map())

@hf.timing
def part1(input):
    vm = VentMap(input)
    return vm.get_intersections()

@hf.timing
def part2(input):
    vm = VentMap(input, True)
    return vm.get_intersections()

## Unit tests ########################################################

@pytest.fixture
def input():
    return [(Coord(0,9),Coord(5,9)),
            (Coord(8,0),Coord(0,8)),
            (Coord(9,4),Coord(3,4)),
            (Coord(2,2),Coord(2,1)),
            (Coord(7,0),Coord(7,4)),
            (Coord(6,4),Coord(2,0)),
            (Coord(0,9),Coord(2,9)),
            (Coord(3,4),Coord(1,4)),
            (Coord(0,0),Coord(8,8)),
            (Coord(5,5),Coord(8,2))]

def test_VentMap_a(input):
    vm = VentMap(input)
    assert vm.get_map() == ['.......1..',
                            '..1....1..',
                            '..1....1..',
                            '.......1..',
                            '.112111211',
                            '..........',
                            '..........',
                            '..........',
                            '..........',
                            '222111....']
def test_VentMap_b(input):
    vm = VentMap(input, True)
    assert vm.get_map() == ['1.1....11.',
                            '.111...2..',
                            '..2.1.111.',
                            '...1.2.2..',
                            '.112313211',
                            '...1.2....',
                            '..1...1...',
                            '.1.....1..',
                            '1.......1.',
                            '222111....']

def test_VentMap_intersections_a(input):
    vm = VentMap(input)
    assert vm.get_intersections() == 5

def test_VentMap_intersections_b(input):
    vm = VentMap(input, True)
    assert vm.get_intersections() == 12

## Main ########################################################

if __name__ == '__main__':
    input = []
    with open(sys.argv[1]) as f:
        for row in f.readlines():
            row = row.strip().split(' -> ')
            start = Coord(*map(int, row[0].split(',')))
            end = Coord(*map(int, row[1].split(',')))
            input.append([start, end])


    print("Advent of code day 5")
    print("Part1 result: {}".format(part1(input.copy())))
    print("Part2 result: {}".format(part2(input.copy())))
