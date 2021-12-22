#!/usr/bin/env python3

# By Jakob Ruhe 2021-12-21

import os
import re
import unittest
from collections import defaultdict


def solve1(pos1, pos2):
    s1, s2 = 0, 0
    pos1 -= 1
    pos2 -= 1
    dice_throws = 0
    while True:
        for i in range(3):
            dice_throws += 1
            pos1 += dice_throws
        s1 += (pos1 % 10) + 1
        if s1 >= 1000:
            return dice_throws * s2
        for i in range(3):
            dice_throws += 1
            pos2 += dice_throws
        s2 += (pos2 % 10) + 1
        if s2 >= 1000:
            return dice_throws * s1


def dice3():
    """Returns a dict with keys representing the outcome, which in this
    case is the sum of throwing 3 3-sided dices. The values of the dict
    represents the number of times this outcome happens."""
    outcome = defaultdict(int)
    for d1 in range(3):
        for d2 in range(3):
            for d3 in range(3):
                outcome[d1 + d2 + d3 + 3] += 1
    return outcome


def number_of_wins(pos1, pos2, score1, score2, final_score, cache):
    c = cache.get((pos1, pos2, score1, score2))
    if c is not None:
        return c
    w1_tot = 0
    w2_tot = 0
    for k1, v1 in dice3().items():
        p1 = (pos1 + k1) % 10
        s1 = score1 + p1 + 1
        if s1 >= final_score:
            w1_tot += v1
            continue
        for k2, v2 in dice3().items():
            p2 = (pos2 + k2) % 10
            s2 = score2 + p2 + 1
            if s2 >= final_score:
                w2_tot += v2 * v1
                continue
            w1, w2 = number_of_wins(p1, p2, s1, s2, final_score, cache)
            cache[(p1, p2, s1, s2)] = (w1, w2)
            w1_tot += w1 * v1 * v2
            w2_tot += w2 * v1 * v2
    return w1_tot, w2_tot


def solve2(pos1, pos2, final_score=21):
    w1, w2 = number_of_wins(pos1 - 1, pos2 - 1, 0, 0, final_score, {})
    return max(w1, w2)


# Execute tests with:
# python3 -m unittest dayX
class TestThis(unittest.TestCase):
    input = """
"""

    def test1(self):
        self.assertEqual(solve1(4, 8), 739785)

    def test2(self):
        self.assertEqual(number_of_wins(0, 0, 0, 0, 4, {}), (27, 0))
        self.assertEqual(solve2(4, 8), 444356092776315)


if __name__ == "__main__":
    # No parsing today, instead the start positions are just entered here
    # directly.
    pos1, pos2 = 10, 3
    print(solve1(pos1, pos2))
    print(solve2(pos1, pos2))
