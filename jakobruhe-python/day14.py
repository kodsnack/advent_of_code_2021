#!/usr/bin/env python3

# By Jakob Ruhe 2021-12-14

import os
import re
import unittest
from collections import Counter


def parse_input(input):
    return input.strip().split("\n")


def count_in(template, steps_left, rules, counter, cache):
    if steps_left == 0 or len(template) == 1:
        for t in template:
            counter[t] += 1
    elif len(template) == 2:
        next_step = (template[0], rules["".join(template)], template[1])
        c = cache.get((next_step, steps_left - 1))
        if c is not None:
            counter += c
        else:
            local_counter = Counter()
            count_in(next_step, steps_left - 1, rules, local_counter, cache)
            cache[(next_step, steps_left - 1)] = local_counter
            counter += local_counter
    else:
        cut = len(template) // 2
        left_tpl = template[0:cut]
        right_tpl = template[cut:]
        mid_tpl = template[cut - 1 : cut + 1]
        count_in(left_tpl, steps_left, rules, counter, cache)
        count_in(right_tpl, steps_left, rules, counter, cache)
        count_in(mid_tpl, steps_left, rules, counter, cache)
        counter[left_tpl[-1]] -= 1
        counter[right_tpl[0]] -= 1


def solve(entries, steps):
    template = list(entries[0])
    rules = {}
    for e in entries[2:]:
        f, t = e.split(" -> ")
        rules[f] = t
    counter = Counter()
    cache = {}
    count_in(template, steps, rules, counter, cache)
    sorted_counter = sorted(counter.values())
    return sorted_counter[-1] - sorted_counter[0]


def solve1(entries):
    return solve(entries, 10)


def solve2(entries):
    return solve(entries, 40)


# Execute tests with:
# python3 -m unittest dayX
class TestThis(unittest.TestCase):
    input = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C
"""

    def test1(self):
        self.assertEqual(solve1(parse_input(self.input)), 1588)

    def test2(self):
        self.assertEqual(solve2(parse_input(self.input)), 2188189693529)


if __name__ == "__main__":
    problem_name = os.path.splitext(os.path.basename(__file__))[0]
    with open(f"input/{problem_name}.txt") as f:
        entries = parse_input(f.read())
    print(solve1(entries))
    print(solve2(entries))
