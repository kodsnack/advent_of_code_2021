#!/usr/bin/env python3

# By Jakob Ruhe 2021-12-20

import os
import re
import unittest


def parse_input(input):
    return input.strip()


def get_output(x, y, back, image, algo):
    s = 0
    W, H = len(image[0]), len(image)
    for i in range(9):
        dx = i % 3 - 1
        dy = i // 3 - 1
        is_inside = x + dx >= 0 and x + dx < W and y + dy >= 0 and y + dy < H
        s <<= 1
        s |= image[y + dy][x + dx] if is_inside else back
    return algo[s]


def enhance(image, algo, steps):
    back = 0
    for step in range(steps):
        W, H = len(image[0]), len(image)
        output = [
            [get_output(x, y, back, image, algo) for x in range(-1, W + 1)]
            for y in range(-1, H + 1)
        ]
        back = algo[0] if back == 0 else algo[-1]
        image = output
    return image, back


def count_lit_pixels(image):
    return sum(map(sum, image))


def solve(indata, steps):
    algo_str, image_str = indata.split("\n\n")
    algo_str = algo_str.replace("\n", "")
    image_str = image_str.split("\n")

    algo = [1 if c == "#" else 0 for c in algo_str]
    W, H = len(image_str[0]), len(image_str)

    image = [[1 if image_str[y][x] == "#" else 0 for x in range(W)] for y in range(H)]

    output, back = enhance(image, algo, steps)

    assert back == 0

    return count_lit_pixels(output)


def solve1(indata):
    return solve(indata, 2)


def solve2(indata):
    return solve(indata, 50)


# Execute tests with:
# python3 -m unittest dayX
class TestThis(unittest.TestCase):
    input = """
..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..##
#..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###
.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#.
.#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#.....
.#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#..
...####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.....
..##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#

#..#.
#....
##..#
..#..
..###
"""

    def test1(self):
        self.assertEqual(solve1(parse_input(self.input)), 35)

    def test2(self):
        self.assertEqual(solve2(parse_input(self.input)), 3351)


if __name__ == "__main__":
    problem_name = os.path.splitext(os.path.basename(__file__))[0]
    with open(f"input/{problem_name}.txt") as f:
        entries = parse_input(f.read())
    print(solve1(entries))
    print(solve2(entries))
