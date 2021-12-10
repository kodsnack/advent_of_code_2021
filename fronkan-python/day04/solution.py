from pathlib import Path

import numpy as np

from aoc_lib.input_readers import read_chunks


def puzzle1(input_file: Path):
    bingo_draws, bingo_boards = _load_bingo_data(input_file)
    for round, draw in enumerate(bingo_draws, start=1):
        for board in bingo_boards:
            match_matrix = np.isin(board, bingo_draws[0:round])
            if _has_bingo(match_matrix):
                return np.sum(board[~match_matrix]) * draw


def puzzle2(input_file: Path):
    bingo_draws, bingo_boards = _load_bingo_data(input_file)
    for round, draw in enumerate(bingo_draws, start=1):
        winning_board_id_to_score = {}
        for board in bingo_boards:
            match_matrix = np.isin(board, bingo_draws[0:round])
            if _has_bingo(match_matrix):
                winning_board_id_to_score[id(board)] = (
                    np.sum(board[~match_matrix]) * draw
                )

        bingo_boards = [
            board
            for board in bingo_boards
            if id(board) not in winning_board_id_to_score
        ]

        if len(bingo_boards) == 0:
            assert len(winning_board_id_to_score) == 1
            last_winning_board_score = next(iter(winning_board_id_to_score.values()))
            return last_winning_board_score


def _load_bingo_data(input_file: Path) -> tuple[np.ndarray, list[np.ndarray]]:
    chunks = read_chunks(input_file)
    bingo_draws = np.array([int(num) for num in chunks[0][0].split(",")])
    bingo_boards = [_parse_board("\n".join(chunk)) for chunk in chunks[1:]]
    return bingo_draws, bingo_boards


def _parse_board(starting_board: str) -> np.ndarray:
    return np.fromstring(starting_board, sep=" ", dtype=int).reshape(5, 5)


def _has_bingo(match_matrix: np.ndarray) -> bool:
    matching_rows = np.all(match_matrix, axis=1)
    matching_cols = np.all(match_matrix, axis=0)
    if np.any(matching_rows) or np.any(matching_cols):
        return True
    return False


if __name__ == "__main__":
    print("Day 4")
    input_file = Path(__file__).parent / "input.txt"
    # input_file = Path(__file__).parent / "example_input.txt"
    print("Puzzle 1:", puzzle1(input_file))
    print("Puzzle 2:", puzzle2(input_file))
