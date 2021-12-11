from pathlib import Path

import numpy as np

def puzzle1(input_file: Path):
    positions = np.fromstring(input_file.read_text(), sep=",", dtype=int)
    dm = _distance_matrix(positions)
    return np.sum(dm, axis=1, dtype=int).min()


def puzzle2(input_file: Path):
    """Solution for second puzzle using arithmetic series.

    As we have a sum that increases with a constant value (+1),
    we can treat this as a arithmetic series. The formula is
    (n(a_0 + a_n))/2.

    where a_0 is the first value, a_n is the n:th value and n is the
    number of values in the series.

    Problem specific simplifications:
    1) The series has +1 as the step, aka a_n - a_(n-1) == 1.
    2) It always start at 1, as moving 1 step uses up 1 fuel.

    1) Gives us that a_0 + a_n == 1 + a_n
    1) and 2) gives us that n is exactly a_n.

    final formula
    (a_n(a_n+1))/2
    
    Using numpy we can use the distance matrix from part 1. We just swap a_n
    for our distance matrix dm. Note that we use elementwise multiplication for
    the matrix and not matrix-multiplication. Then we need to sum each row and
    find the lowest value, just like in the first puzzle.
    """
    
    positions = np.fromstring(input_file.read_text(), sep=",", dtype=int)
    dm = _distance_matrix(positions)
    # Note that multiplication is elementwise-multiplication
    fuel_cost_matrix = (dm*(dm+1))/2
    return np.sum(fuel_cost_matrix, axis=1, dtype=int).min()

def _distance_matrix(positions: np.ndarray) -> np.ndarray:
    """Returns a matrix where each row is the distances for to this position.

    Assume we have 3 submarines with positions=[0, 2, 4]. Then the distance matrix
    will have 5 rows, one for each possible postion: [0, 1, 2, 3, 4].
    It will have 3 columns one for each submarine, such that the third row
    is the distance for each submarine to the possition 2 
    (which is the third element in the array).
    """
    r = np.arange(0, positions.max())
    return np.abs(r[:, None] - positions[None, :])

if __name__ == "__main__":
    print("Day 7")
    input_file = Path(__file__).parent / "input.txt"
    # input_file = Path(__file__).parent / "example_input.txt"
    print("Puzzle 1:", puzzle1(input_file))
    print("Puzzle 2:", puzzle2(input_file))