#!/usr/bin/env python3

# By Jakob Ruhe 2021-12-12

import os
import unittest
from collections import defaultdict


def parse_input(indata):
    caves = defaultdict(list)
    for e in indata.strip().split("\n"):
        c1, c2 = e.split("-")
        caves[c1].append(c2)
        caves[c2].append(c1)
    return caves


def walk(pos, caves, visited, allow_revisit_small):
    if pos == "end":
        return 1
    count = 0
    visited.append(pos)
    for c in caves[pos]:
        if c == "start":
            continue
        is_small = c.islower()
        visited_before = c in visited
        revisiting_small = is_small and visited_before
        allow_visit = not is_small or not visited_before or allow_revisit_small
        allow_revisit_small_c = allow_revisit_small and not revisiting_small
        if allow_visit:
            count += walk(c, caves, visited, allow_revisit_small_c)
    visited.pop()
    return count


def solve1(caves):
    return walk("start", caves, [], False)


def solve2(caves):
    return walk("start", caves, [], True)


# Execute tests with:
# python3 -m unittest dayX
class TestThis(unittest.TestCase):
    input1 = """start-A
start-b
A-c
A-b
b-d
A-end
b-end
"""
    input2 = """dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc
"""
    input3 = """fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW
"""

    def test1(self):
        self.assertEqual(solve1(parse_input(self.input1)), 10)
        self.assertEqual(solve1(parse_input(self.input2)), 19)
        self.assertEqual(solve1(parse_input(self.input3)), 226)

    def test2(self):
        self.assertEqual(solve2(parse_input(self.input1)), 36)
        self.assertEqual(solve2(parse_input(self.input2)), 103)
        self.assertEqual(solve2(parse_input(self.input3)), 3509)


if __name__ == "__main__":
    problem_name = os.path.splitext(os.path.basename(__file__))[0]
    with open(f"input/{problem_name}.txt") as f:
        entries = parse_input(f.read())
    print(solve1(entries))
    print(solve2(entries))
