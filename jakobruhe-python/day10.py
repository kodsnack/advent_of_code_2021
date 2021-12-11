#!/usr/bin/env python3

# By Jakob Ruhe 2021-12-10

import os
import unittest


verbose = False
open_tokens = "([{<"
close_tokens = ")]}>"


def debug(str):
    if verbose:
        print(str)


def parse_input(input):
    return input.strip().split("\n")


def parse(expr):
    stack = []
    for pos, tok in enumerate(expr):
        if tok in close_tokens:
            expect = close_tokens[open_tokens.index(stack.pop())]
            if tok != expect:
                return pos, stack, expect
        elif tok in open_tokens:
            stack.append(tok)
        else:
            raise (f"Expr {expr} at {pos}: Bad token {tok}")
    return len(expr), stack, None


def solve1(entries):
    token_scores = (3, 57, 1197, 25137)
    scores = []
    for e in entries:
        pos, stack, expect = parse(e)
        if pos == len(e):
            debug(f"Expr {e}: skipped")
            continue
        scores.append(token_scores[close_tokens.index(e[pos])])
        debug(
            f"Expr {e} at {pos}: Expected {expect} got {e[pos]} which gives {scores[-1]} points"
        )
    return sum(scores)


def solve2(entries):
    token_scores = (1, 2, 3, 4)
    scores = []
    for e in entries:
        pos, stack, _ = parse(e)
        if pos != len(e):
            debug(f"Expr {e}: skipped")
            continue
        score = 0
        for s in reversed(stack):
            score *= 5
            score += token_scores[open_tokens.index(s)]
        debug(f"Expr {e}: score: {score}")
        scores.append(score)
    return sorted(scores)[len(scores) // 2]


# Execute tests with:
# python3 -m unittest dayX
class TestThis(unittest.TestCase):
    input = """
[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]
"""

    def test1(self):
        self.assertEqual(solve1(parse_input(self.input)), 26397)

    def test2(self):
        self.assertEqual(solve2(parse_input(self.input)), 288957)


if __name__ == "__main__":
    problem_name = os.path.splitext(os.path.basename(__file__))[0]
    with open(f"input/{problem_name}.txt") as f:
        entries = parse_input(f.read())
    print(solve1(entries))
    print(solve2(entries))
