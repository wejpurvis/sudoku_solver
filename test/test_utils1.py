# Unit tests for parse_grid function in utils.py
import numpy as np
from src.utils import parse_grid
import pytest


def test_parseGrid_valid_input():
    valid_sudoku = """
000|801|008
000|000|043
500|000|000
---+---+---
000|070|800
000|000|100
020|030|000
---+---+---
600|000|075
003|400|000
000|200|600
"""

    expected = [
        [0, 0, 0, 8, 0, 1, 0, 0, 8],
        [0, 0, 0, 0, 0, 0, 0, 4, 3],
        [5, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 7, 0, 8, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 2, 0, 0, 3, 0, 0, 0, 0],
        [6, 0, 0, 0, 0, 0, 0, 7, 5],
        [0, 0, 3, 4, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 6, 0, 0],
    ]

    assert np.all(expected == parse_grid(valid_sudoku))


def test_parseGrid_invalid_input_type():
    sudoku = 123
    with pytest.raises(TypeError):
        parse_grid(sudoku)


def test_parseGrid_invalid_input_length():
    sudoku = """
000|007|000
000|009|504
000|050|169
---+---+---
080|000|305
075|000|290
406|000|080
---+---+---
762|080|000
103|900|000
000|600|0000
"""
    with pytest.raises(ValueError):
        parse_grid(sudoku)


def test_parseGrid_invalid_input_characters():
    sudoku = """
000|007|000
000|009|504
000|050|169
---+---+---
080|000|305
075|000|290
406|000|080
---+---+---
762|080|000
103|900|0c0
000|600|000
"""
    with pytest.raises(ValueError):
        parse_grid(sudoku)
