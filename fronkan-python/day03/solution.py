from pathlib import Path
from statistics import mode
from typing import Generator, Iterable, Iterator
from collections import Counter


def puzzle1(input_file: Path):
    diagnostics_report = input_file.read_text().splitlines()
    gamma_rate = calc_gamma_rate(diagnostics_report)
    epsilon_rate = calc_epislon_rate(diagnostics_report)
    return gamma_rate * epsilon_rate


def calc_gamma_rate(diagnostics_report: list[str]) -> int:
    col_len = len(diagnostics_report[0])
    gamma_binary = "".join(
        _most_common_bit(_get_column(diagnostics_report, col_idx))
        for col_idx in range(col_len)
    )
    return int(gamma_binary, base=2)


def calc_epislon_rate(diagnostics_report: list[str]) -> int:
    col_len = len(diagnostics_report[0])
    gamma_binary = "".join(
        _least_common_bit(_get_column(diagnostics_report, col_idx))
        for col_idx in range(col_len)
    )
    return int(gamma_binary, base=2)


def puzzle2(input_file: Path):
    diagnostics_report = input_file.read_text().splitlines()
    oxygen_generator_rate = calc_oxygen_generator_rate(diagnostics_report)
    co2_scrubber_rate = calc_co2_scrubber_rate(diagnostics_report)
    return oxygen_generator_rate * co2_scrubber_rate


def calc_oxygen_generator_rate(diagnostics_report: list[str]) -> int:
    col_idx = 0
    while len(diagnostics_report) > 1:
        bit_criteria = _most_common_bit(_get_column(diagnostics_report, col_idx))
        diagnostics_report = [
            line for line in diagnostics_report if line[col_idx] == bit_criteria
        ]
        col_idx += 1
    if len(diagnostics_report) == 0:
        raise ValueError("Diagnostics report contains no oxygen generator rate")
    return int(diagnostics_report[0], base=2)


def calc_co2_scrubber_rate(diagnostics_report: list[str]) -> int:
    col_idx = 0
    while len(diagnostics_report) > 1:
        bit_criteria = _least_common_bit(_get_column(diagnostics_report, col_idx))
        diagnostics_report = [
            line for line in diagnostics_report if line[col_idx] == bit_criteria
        ]
        col_idx += 1
    if len(diagnostics_report) == 0:
        raise ValueError("Diagnostics report contains no CO2 scrubber rate")
    return int(diagnostics_report[0], base=2)


def _get_column(lines: list[str], col_idx: int) -> list[str]:
    return [line[col_idx] for line in lines]


def _most_common_bit(bin_array: Iterable[str]) -> str:
    counts = Counter(bin_array)
    return "0" if counts["0"] > counts["1"] else "1"


def _least_common_bit(bin_array: Iterable[str]):
    counts = Counter(bin_array)
    return "1" if counts["1"] < counts["0"] else "0"


if __name__ == "__main__":
    print("Day 3")
    input_file = Path(__file__).parent / "input.txt"
    # input_file = Path(__file__).parent / "example_input.txt"
    print("Puzzle 1:", puzzle1(input_file))
    print("Puzzle 2:", puzzle2(input_file))
