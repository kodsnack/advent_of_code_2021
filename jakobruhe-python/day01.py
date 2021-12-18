#!/usr/bin/env python3

# By Jakob Ruhe 2021-12-01

import os

def parse_input(input):
    return list(map(int, input.strip().split("\n")))

def solve1(entries):
    count = 0
    last = entries[0]
    for e in entries[1:]:
        if e > last:
            count += 1
        last = e
    return count

def solve2(entries):
    count = 0
    size = len(entries)
    last = sum(entries[0:3])
    for i in range(size - 3):
        cur = sum(entries[i+1:i+4])
        if cur > last:
            count += 1
        last = cur
    return count

if __name__ == "__main__":
    problem_name = os.path.splitext(os.path.basename(__file__))[0]
    with open(f"input/{problem_name}.txt") as f:
        entries = parse_input(f.read())
    print(solve1(entries))
    print(solve2(entries))
