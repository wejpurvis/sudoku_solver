# Unit tests for displaySudoky function in utils.py
from src.utils import displaySudoku
import pytest


def test_displaySudoku_valid_input():
    board = [
        [0, 0, 0, 0, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 0, 9, 5, 0, 4],
        [0, 0, 0, 0, 5, 0, 1, 6, 9],
        [0, 8, 0, 0, 0, 3, 0, 5, 0],
        [0, 7, 5, 0, 0, 0, 2, 9, 0],
        [4, 0, 6, 0, 0, 0, 0, 8, 0],
        [7, 6, 2, 0, 8, 0, 0, 0, 0],
        [1, 0, 3, 9, 0, 0, 0, 0, 0],
        [0, 0, 0, 6, 0, 0, 0, 0, 0],
    ]
    expected_output = "000|007|000\n000|009|504\n000|050|169\n---+---+---\n080|003|050\n075|000|290\n406|000|080\n---+---+---\n762|080|000\n103|900|000\n000|600|000\n"
    assert displaySudoku(board) == expected_output


def test_displaySudoku_invalid_input_type():
    board = "invalid"
    with pytest.raises(TypeError):
        displaySudoku(board)


def test_displaySudoku_invalid_input_length():
    board = [
        [0, 0, 0, 0, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 0, 9, 5, 0, 4],
        [0, 0, 0, 0, 5, 0, 1, 6, 9],
        [0, 8, 0, 0, 0, 3, 0, 5, 0],
        [0, 7, 5, 0, 0, 0, 2, 9, 0],
        [4, 0, 6, 0, 0, 0, 0, 8, 0],
        [7, 6, 2, 0, 8, 0, 0, 0, 0],
        [1, 0, 3, 9, 0, 0, 0, 0, 0],
    ]
    with pytest.raises(ValueError):
        displaySudoku(board)


def test_displaySudoku_invalid_input_values():
    board = [
        [0, 0, 0, 0, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 0, 9, 5, 0, 4],
        [0, 0, 0, 0, 5, 0, 1, 6, 9],
        [0, 8, 0, 0, 0, 3, 0, 5, 0],
        [0, 7, 5, 0, 0, 0, 2, 9, 0],
        [4, 0, 6, 0, 0, 0, 0, 8, 0],
        [7, 6, 2, 0, 8, 0, 0, 0, 0],
        [1, 0, 3, 9, 0, 0, 0, 0, 10],
        [0, 0, 0, 6, 0, 0, 0, 0, 0],
    ]
    with pytest.raises(ValueError):
        displaySudoku(board)
