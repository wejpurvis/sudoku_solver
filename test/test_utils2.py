# Unit tests for isValidSudoku function in utils.py
from src.utils import validate_board
import numpy as np


def test_validate_board_valid():
    board = np.array(
        [
            [0, 0, 0, 8, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 4, 3],
            [5, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 7, 0, 8, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 2, 0, 0, 3, 0, 0, 0, 0],
            [6, 0, 0, 0, 0, 0, 0, 7, 5],
            [0, 0, 3, 4, 0, 0, 0, 0, 0],
            [0, 0, 0, 2, 0, 0, 6, 0, 0],
        ]
    )

    assert validate_board(board) is True


def test_validate_board_invalid():
    board = np.array(
        [
            [0, 0, 0, 8, 0, 1, 0, 0, 8],  # two 8s in row 0
            [0, 0, 0, 0, 0, 0, 0, 4, 3],
            [5, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 7, 0, 8, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 2, 0, 0, 3, 0, 0, 0, 0],
            [6, 0, 0, 0, 0, 0, 0, 7, 5],
            [0, 0, 3, 4, 0, 0, 0, 0, 0],
            [0, 0, 0, 2, 0, 0, 6, 0, 0],
        ]
    )

    assert validate_board(board)[0] is False


def test_validate_board_invalid_type():
    board = "Sudoku board"
    try:
        validate_board(board)
        assert False  # TypeError should be raised
    except TypeError:
        assert True
