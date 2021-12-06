#!/usr/bin/env python3

import helpfunctions as hf
import sys, pytest
from collections import namedtuple

Coord = namedtuple('Coord', ['x', 'y'])


class VentMap():
    def __init__(self, input: list[tuple[Coord, Coord]]):
        size = max(max(max(input))) + 1
        self.map = [[0] * size for i in range(size)]
        # import pdb; pdb.set_trace()
        for (start, end) in input:
            x_range = None
            y_range = None
            if start.x == end.x:
                y_range = range(min(start.y, end.y), max(start.y,end.y)+1)
                x_range = [start.x] * len(y_range)
            if start.y == end.y:
                x_range = range(min(start.x, end.x), max(start.x,end.x)+1)
                y_range = [start.y] * len(x_range)
            if x_range:
                for x, y in zip(x_range, y_range):
                    self.map[y][x] += 1
                    # print(self)

    def get_map(self):
        return [''.join(map(str, row)).replace('0','.') for row in self.map]

    def get_intersections(self):
        return sum(sum(item > 1 for item in row) for row in self.map)
   
    def __repr__(self):
        return str(self.get_map())
        
    def __str__(self):
        return '\n'.join(self.get_map())

@hf.timing
def part1(data):
    input = []
    for row in data:
        row = row.split(' -> ')
        start = Coord(*map(int, row[0].split(',')))
        end = Coord(*map(int, row[1].split(',')))
        input.append([start, end])
    vm = VentMap(input)
    return vm.get_intersections()

@hf.timing
def part2(data):
    return 0

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

def test_VentMap(input):
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

def test_VentMap_intersections(input):
    vm = VentMap(input)
    assert vm.get_intersections() == 5

## Main ########################################################

if __name__ == '__main__':

    print("Advent of code day X")
    print("Part1 result: {}".format(part1(hf.readFile(sys.argv[1]))))
    print("Part2 result: {}".format(part2(hf.getIntsFromFile(sys.argv[1]))))
