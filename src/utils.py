"""
| This module contains utility functions that are used throughout the project.
| :code:`parse_grid()` converts a text-based suduko grid into a numpy array
   ready for processing.
  :code:`validate_board()` checks if a sudoku board is valid (*note*: a valid sudoku
   does not necessarily mean that the sudoku is solvable). If the board is invalid, the
    row and column of the invalid cells are returned.
  :code:`highlight_errors()` highlights the invalid cells in red.
  :code:`display_sudoku()` converts a list of lists into a text-based
   suduko grid for display purposes.
"""

import numpy as np
from typing import Union


def parse_grid(sudoku: str) -> np.array:
    """
    Convert text-based suduko grid into a numpy array.
    This function allows for easier manipulation of the sudoku grid by accessing
    numbers via their row (:code:`[i]`) and column (:code:`[j]`) index.

    Parameters
    ----------
    sudoku: str
        Text-based grid representation of Sudoku. Empty cells should be denoted
        with a :code:`0`, with :code:`|` and :code:`-` used to seperate subgrid
        columns and rows, respectively.
        The intersections of each subgrid should be marked with :code:`+`.

        Example:

        ::

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
            000|600|000

    Returns
    ----------
    sudoku_list : np.darray
        A numpy array where elements can be accessed by row [i] & column [j].

    Raises
    ----------
    TypeError
        If input is not a string.
    ValueError
        If input is not an 11x11 grid, including '|', '-', and '+' characters.
    """
    # Check if input is valid (string)
    if not isinstance(sudoku, str):
        raise TypeError("Input must be a string")

    # Flatten input string into a list
    sudoku_list_raw = []
    for char in sudoku:
        if char != "\n":
            sudoku_list_raw.append(char)

    # Check if input is valid (length)
    if len(sudoku_list_raw) != 11 * 11:
        raise ValueError(
            "Invalid sudoku input! "
            "Sudoku must be an 11x11 grid (don't forget to seperate grids "
            "with |, -, and + signs)"
        )

    # Convert list into a numpy array
    sudoku_list = [int(char) for char in sudoku_list_raw if char.isdigit()]
    sudoku_array = np.array(sudoku_list, dtype=np.intc).reshape(9, 9)

    return sudoku_array


def validate_board(sudoku: np.array) -> Union[bool, list[tuple[int, int]]]:
    """
    Given a 2D numpy array representing a sudoku board, check if the board is valid.
    Validity of sudoku is based off the following rules:

    1) Each row must contain the digits 1-9 without repetition.
    2) Each column must contain the digits 1-9 without repetition.
    3) Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without
       repetition

    *Note*: a valid sudoku does not necessarily mean that the sudoku is solvable.

    If the board is valid, True is returned. If the board is invalid, False and the row
    and column of the invalid cells are returned.

    Parameters
    ----------
    sudoku : np.array
        2D numpy array representing a sudoku board

    Returns
    ---------
    bool
        True if board is valid, False otherwise
    list[tuple[int, int]]
        List of tuples containing the row and column of the invalid cells. Empty list
        if board is valid.

    Raises
    ---------
    TypeError
        If input is not a numpy array
    """
    # Check if input is valid (type)
    if type(sudoku) != np.ndarray:
        raise TypeError("Input must be a numpy array")

    # Convert numpy array to list of lists
    sudoku_list = [list(row) for row in sudoku]

    # Check validity of sudoku
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    block = [[set() for _ in range(3)] for _ in range(3)]
    invalid_cells = []

    for i in range(9):  # iterate over rows
        for j in range(9):  # iterate over columns
            element = sudoku_list[i][j]
            if element == 0:
                continue
            if (
                (element in rows[i])
                or (element in cols[j])
                or (element in block[i // 3][j // 3])
            ):
                invalid_cells.append((i, j))
            rows[i].add(element)
            cols[j].add(element)
            block[i // 3][j // 3].add(element)

    if len(invalid_cells) == 0:
        return True
    else:
        return False, invalid_cells


def highlight_errors(sudoku: np.array, invalid_cells: list[tuple[int, int]]) -> None:
    """
    Given a 2D numpy array representing a sudoku board and a list of invalid cells for
    the given board, highlight the invalid cells in red.

    Parameters
    ----------
    sudoku : np.array
        2D numpy array representing a sudoku board
    invalid_cells : list[tuple[int, int]]
        List of tuples containing the row and column of the invalid cells.

    """
    # Define ANSI escape codes for text colours
    RED = "\033[91m"
    RESET = "\033[0m"

    # Convert numpy array to list of lists
    sudoku_list = [list(row) for row in sudoku]

    # Convert list of lists into a string
    sudoku_str = ""
    for row in sudoku_list:
        for idx, val in enumerate(row):
            # Highlight invalid cells in red
            if (sudoku_list.index(row), idx) in invalid_cells:
                char_str = f"{RED}{val}{RESET}"
            else:
                char_str = str(val)
            if idx == 2 or idx == 5:
                sudoku_str += char_str + "|"
            else:
                sudoku_str += char_str
        sudoku_str += "\n"
        if row == sudoku_list[2] or row == sudoku_list[5]:
            sudoku_str += "---+---+---\n"
    print(sudoku_str)


def display_sudoku(board: list[list[int]]) -> str:
    """
    Reverse of parse_grid: displays sudoku board given as a list in a readable format.

    Parameters
    ----------
    board : list of list
        List of list where elements can be accessed by row [i] & column [j]

    Returns
    ---------
    sudoku : str
        Text-based grid where empty cells are represented by 0, each subgrid is
        seperated by | and each row is seperated by - and +

        Example:

        ::

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
            000|600|000
    Raises
    ---------
    TypeError
        If input is not a list of lists of ints
    ValueError
        If input is not 9x9 or if cells contains values outside of 0-9

    """

    # Check if input is valid (list of list)
    if type(board) != list:
        raise TypeError("Input must be a list")
    if type(board[0]) != list:
        raise TypeError("Input must be a list of lists")

    # Check if input is valid (length)
    if len(board) != 9:
        raise ValueError("Input grid must be 9x9")
    for row in board:
        if len(row) != 9:
            raise ValueError("Input grid must be 9x9")

    # Check if input is valid (values)
    for row in board:
        for val in row:
            if type(val) != int:
                raise TypeError("Input must be a list of lists of ints")
            if val < 0 or val > 9:
                raise ValueError("Input must be a list of lists of ints from 0-9")

    # Convert list of lists into a string
    sudoku = ""
    for row in board:
        for val, idx in enumerate(row):
            if val == 2 or val == 5:
                sudoku += str(idx) + "|"
            else:
                sudoku += str(idx)
        sudoku += "\n"
        if row == board[2] or row == board[5]:
            sudoku += "---+---+---\n"

    return sudoku
