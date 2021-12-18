from collections import Counter
from pathlib import Path


def puzzle1(input_file: Path):
    return _run_simulation_smart(input_file, 80)


def puzzle2(input_file: Path):
    return _run_simulation_smart(input_file, 256)


def _run_simulation_smart(input_file: Path, steps: int):
    day2count = Counter(
        int(start_timer) for start_timer in input_file.read_text().strip().split(",")
    )
    for step in range(steps):
        day2count = {day - 1: count for day, count in day2count.items()}
        if -1 in day2count:
            num_birthing_fishes = day2count[-1]
            day2count[6] = day2count.get(6, 0) + num_birthing_fishes
            day2count[8] = num_birthing_fishes
            del day2count[-1]
    return sum(day2count.values())


if __name__ == "__main__":
    print("Day 6")
    input_file = Path(__file__).parent / "input.txt"
    # input_file = Path(__file__).parent / "example_input.txt"
    print("Puzzle 1:", puzzle1(input_file))
    print("Puzzle 2:", puzzle2(input_file))
