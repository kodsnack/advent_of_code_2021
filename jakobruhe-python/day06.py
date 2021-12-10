#!/usr/bin/env python3

# By Jakob Ruhe 2021-12-06

import os
import unittest
from collections import defaultdict


def parse_input(input):
    return list(map(int, input.strip().split(",")))


def solve(entries, days):
    lanterns = defaultdict(int)
    for e in entries:
        lanterns[e] += 1
    for day in range(days):
        lanterns_next = defaultdict(int)
        for k, v in lanterns.items():
            if k == 0:
                lanterns_next[8] += v
                lanterns_next[6] += v
            else:
                lanterns_next[k - 1] += v
        lanterns = lanterns_next
    return sum(lanterns.values())


def solve1(entries):
    return solve(entries, 80)


def solve2(entries):
    return solve(entries, 256)


# Execute tests with:
# python3 -m unittest dayX
class TestThis(unittest.TestCase):
    input = """3,4,3,1,2"""
    def test1(self):
        self.assertEqual(solve(parse_input(self.input), 18), 26)
        self.assertEqual(solve(parse_input(self.input), 80), 5934)
    def test2(self):
        self.assertEqual(solve(parse_input(self.input), 256), 26984457539)


if __name__ == "__main__":
    problem_name = os.path.splitext(os.path.basename(__file__))[0]
    with open(f"input/{problem_name}.txt") as f:
        entries = parse_input(f.read())
    print(solve1(entries))
    print(solve2(entries))
