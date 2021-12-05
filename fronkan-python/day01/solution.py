from pathlib import Path

def puzzle1(input_file: Path):
    values = [int(line) for line in input_file.read_text().splitlines()]
    prev_val = values[0]
    cnt = 0
    for val in values[1:]:
        if val > prev_val:
            cnt += 1
        prev_val = val
    return cnt


def puzzle2(input_file: Path):
    values = [int(line) for line in input_file.read_text().splitlines()]
    windows = _windowed_iter(values)
    prev_val = sum(next(windows))
    cnt = 0
    for window in windows:
        val = sum(window)
        if val > prev_val:
            cnt += 1
        prev_val = val
    return cnt

def _windowed_iter(values: list[int]):
    for center_idx in range(1, len(values)-1):
        yield values[center_idx-1:center_idx+2]

if __name__ == "__main__":
    print("Day 1")
    input_file = Path(__file__).parent / "input.txt"
    print("Puzzle 1:", puzzle1(input_file))
    print("Puzzle 2:", puzzle2(input_file))