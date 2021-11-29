from aocd.models import Puzzle
from os import path, getcwd
from sys import argv
import re

def getYear():
    yearPattern = re.compile(r"y(\d+)")
    m = yearPattern.search(getcwd())
    return int(m.group(1))

def getDay():
    dayPattern = re.compile(r"d(\d+)")
    d = dayPattern.search(argv[0])
    return int(d.group(1))

def getPuzzle():
    return Puzzle(year=getYear(), day=getDay())

def submitSecure(puzzle, part, answer):
    check = input(f"Are you sure you want to submit '{answer}' as answer to part {part}? ")
    if check.lower() in ["y", "yes"]:
        if part.lower() == "a":
            print(f"Submitting puzzle.answer_a = {answer}")
            puzzle.answer_a = answer
        if part.lower() == "b":
            print(f"Submitting puzzle.answer_b = {answer}")
            puzzle.answer_b = answer
