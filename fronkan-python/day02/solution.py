from pathlib import Path
from dataclasses import dataclass
from typing import Protocol


class SubmarinePositionInterface(Protocol):
    horizontal: int
    depth: int

    def forward(self, change: int):
        pass

    def down(self, change: int):
        pass

    def up(self, change: int):
        pass


@dataclass
class SubmarinePositionP1:
    horizontal: int = 0
    depth: int = 0

    def forward(self, change: int):
        self.horizontal += change

    def down(self, change: int):
        self.depth += change

    def up(self, change: int):
        self.depth -= change


@dataclass
class SubmarinePositionP2:
    horizontal: int = 0
    depth: int = 0
    aim: int = 0

    def forward(self, change: int):
        self.horizontal += change
        self.depth += self.aim * change

    def down(self, change: int):
        self.aim += change

    def up(self, change: int):
        self.aim -= change


def _run_simulation(sub_pos: SubmarinePositionInterface, input_file: Path):
    with open(input_file) as f:
        for line in f:
            command, change = line.split()
            getattr(sub_pos, command)(int(change))
    return sub_pos.horizontal * sub_pos.depth


def puzzle1(input_file: Path):
    return _run_simulation(SubmarinePositionP1(), input_file)


def puzzle2(input_file: Path):
    return _run_simulation(SubmarinePositionP2(), input_file)


if __name__ == "__main__":
    print("Day 2")
    input_file = Path(__file__).parent / "input.txt"
    # input_file = Path(__file__).parent / "example_input.txt"
    print("Puzzle 1:", puzzle1(input_file))
    print("Puzzle 2:", puzzle2(input_file))
