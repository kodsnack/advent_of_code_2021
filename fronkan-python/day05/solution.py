from collections import Counter
from pathlib import Path
from typing import NamedTuple

class Point(NamedTuple):
    x: int
    y: int

    @classmethod
    def from_comma_seperated(cls, csv_str: str) -> "Point":
        x, y  = csv_str.split(",")
        return cls(int(x), int(y))
    
class Line:
    __slots__=["start", "end"]

    def __init__(self, start: Point, end: Point) -> None:
        self.start = start
        self.end = end
    
    @property
    def is_horizontal(self) -> bool:
        return self.start.x == self.end.x

    @property
    def is_vertical(self) -> bool:
        return self.start.y == self.end.y

    @classmethod
    def from_submarine_row(cls, row: str) -> "Line":
        start_str, end_str = row.split(" -> ")
        start = Point.from_comma_seperated(start_str)
        end = Point.from_comma_seperated(end_str)
        return cls(start, end)

    @property
    def points(self) -> list[Point]:
        if self.is_horizontal:
            start_y = min(self.start.y, self.end.y)
            stop_y = max(self.start.y, self.end.y) + 1
            return [Point(self.start.x, y) for y in range(start_y, stop_y)]

        elif self.is_vertical:
            start_x = min(self.start.x, self.end.x)
            stop_x = max(self.start.x, self.end.x) + 1
            return [Point(x, self.start.y) for x in range(start_x, stop_x)]

        else:
            y_range = range(
                self.start.y,
                self.end.y + (1 if self.start.y < self.end.y else -1),
                1 if self.start.y < self.end.y else -1
            )
            x_range = range(
                self.start.x,
                self.end.x + (1 if self.start.x < self.end.x else -1),
                1 if self.start.x < self.end.x else -1
            )
            return [Point(x,y) for x,y in zip(x_range, y_range, strict=True)]
        
 
def puzzle1(input_file: Path):
    with open(input_file) as f:
        points = [
            point
            for row in f
            if (line := Line.from_submarine_row(row)).is_horizontal or line.is_vertical
            for point in line.points
        ]
    return len([point for point, cnt in Counter(points).items() if cnt >= 2])


def puzzle2(input_file: Path):
    with open(input_file) as f:
        points = [
            point
            for row in f
            for point in Line.from_submarine_row(row).points
        ]
    return len([point for point, cnt in Counter(points).items() if cnt >= 2])


if __name__ == "__main__":
    print("Day 5")
    input_file = Path(__file__).parent / "input.txt"
    # input_file = Path(__file__).parent / "example_input.txt"
    print("Puzzle 1:", puzzle1(input_file))
    print("Puzzle 2:", puzzle2(input_file))