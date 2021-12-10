#!/usr/bin/env python3

# By Jakob Ruhe 2021-12-02

import os

def parse_input(input):
    return input.strip().split("\n")

def solve1(entries):
    loc = 0
    depth = 0
    for e in entries:
        op, steps_str = e.split()
        steps = int(steps_str)
        if op == "forward":
            loc += steps
        elif op == "up":
            depth -= steps
        elif op == "down":
            depth += steps
        else:
            raise ValueError(e)
    return loc * depth

def solve2(entries):
    loc = 0
    depth = 0
    aim = 0
    for e in entries:
        op, steps_str = e.split()
        steps = int(steps_str)
        if op == "forward":
            loc += steps
            depth += aim * steps
        elif op == "up":
            aim -= steps
        elif op == "down":
            aim += steps
        else:
            raise ValueError(e)
    return loc * depth

if __name__ == "__main__":
    problem_name = os.path.splitext(os.path.basename(__file__))[0]
    with open(f"input/{problem_name}.txt") as f:
        entries = parse_input(f.read())
    print(solve1(entries))
    print(solve2(entries))
