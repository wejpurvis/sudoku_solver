# Unit tests for parse_grid function in utils.py

from src.utils import parse_grid
import pytest


def test_parse_grid_valid_input():
    sudoku = "200|080|300\n060|070|084\n030|500|209\n---+---+---\n000|105|408\n000|000|000\n402|706|000\n---+---+---\n301|007|040\n720|040|060\n004|010|003"
    expected_output = [
        [2, 0, 0, 0, 8, 0, 3, 0, 0],
        [0, 6, 0, 0, 7, 0, 0, 8, 4],
        [0, 3, 0, 5, 0, 0, 2, 0, 9],
        [0, 0, 0, 1, 0, 5, 4, 0, 8],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [4, 0, 2, 7, 0, 6, 0, 0, 0],
        [3, 0, 1, 0, 0, 7, 0, 4, 0],
        [7, 2, 0, 0, 4, 0, 0, 6, 0],
        [0, 0, 4, 0, 1, 0, 0, 0, 3],
    ]

    assert parse_grid(sudoku) == expected_output


def test_parse_grid_invalid_input_type():
    sudoku = 12345
    with pytest.raises(TypeError):
        parse_grid(sudoku)


def test_parse_grid_invalid_input_length():
    sudoku = "000|007|000\n000|009|504\n000|050|169\n---+---+---\n080|000|305\n075|000|290\n406|000|080\n---+---+---\n762|080|000\n103|900|000\n000|600|0000"
    with pytest.raises(ValueError):
        parse_grid(sudoku)
