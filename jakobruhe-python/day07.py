#!/usr/bin/env python3

# By Jakob Ruhe 2021-12-07

import os
import unittest


def parse_input(input):
    return list(map(int, input.strip().split(",")))


def solve(entries, cost_func):
    min_cost = None
    for depth in range(min(entries), max(entries) + 1):
        cost = sum(cost_func(entries, depth))
        if min_cost is None or cost < min_cost:
            min_cost = cost
        else:
            break
    return min_cost


def cost1(entries, depth):
    return map(lambda e: abs(e - depth), entries)


def solve1(entries):
    return solve(entries, cost1)


def cost2(entries, depth):
    return map(lambda e: sum(range(1 + abs(e - depth))), entries)


def solve2(entries):
    return solve(entries, cost2)


# Execute tests with:
# python3 -m unittest dayX
class TestThis(unittest.TestCase):
    input = """16,1,2,0,4,2,7,1,2,14
"""
    def test1(self):
        self.assertEqual(solve1(parse_input(self.input)), 37)
    def test2(self):
        self.assertEqual(solve2(parse_input(self.input)), 168)

if __name__ == "__main__":
    problem_name = os.path.splitext(os.path.basename(__file__))[0]
    with open(f"input/{problem_name}.txt") as f:
        entries = parse_input(f.read())
    print(solve1(entries))
    print(solve2(entries))
