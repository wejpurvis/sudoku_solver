"""
| This module contains utility functions that are used throughout the project.
| :code:`parse_grid(sudoku)` converts a text-based suduko grid into a list of list ready for processing.
  :code:`isValidSudoku(board)` checks if a sudoku board is valid (*note*: a valid sudoku does not necessarily mean that the sudoku is solvable).
  :code:`displaySudoku(board)` converts a list of lists into a text-based suduko grid for display purposes.
"""


def parse_grid(sudoku):
    """
    Convert text-based suduko grid into a list of list of integers.
    This function allows for easier manipulation of the sudoku grid by accessing numbers via their row (:code:`[i]`) and column (:code:`[j]`) index.

    Parameters
    ----------
    sudoku: str
        Text-based grid representation of Sudoku. Empty cells should be denoted
        with a :code:`0`, with :code:`|` and :code:`-` used to seperate subgrid columns and rows, respectively.
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
    sudoku_list : list[list[int]]
        A list of list where elements can be accessed by row [i] & column [j]. Each sublist represents a row in the grid.

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
            "Input grid must be 11x11, don't forget to seperate girds with |, -, and + signs!"
        )

    # Convert flattened list of strs into a list of list of ints
    sudoku_list = []
    for i in range(11):
        sudoku_list.append([])
        for j in range(11):
            curr_val = sudoku_list_raw[i * 11 + j]
            if curr_val == "|" or curr_val == "-" or curr_val == "+":
                pass
            else:
                sudoku_list[i].append(int(curr_val))

    # Remove empty sublists
    sudoku_list = [row for row in sudoku_list if row != []]

    return sudoku_list


def isValidSudoku(board: list[list[int]]) -> bool:
    """
    Given a list of lists represrenting a sudoku board, check if the board is valid.
    Validity of sudoku is based off the following rules:

    1) Each row must contain the digits 1-9 without repetition.
    2) Each column must contain the digits 1-9 without repetition.
    3) Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition

    *Note*: a valid sudoku does not necessarily mean that the sudoku is solvable.

    Parameters
    ----------
    board : list[list[int]]]
        List of list where elements can be accessed by row [i] & column [j]

    Returns
    ---------
    bool
        True if board is valid, False otherwise

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

    # Check validity of sudoku
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    block = [[set() for _ in range(3)] for _ in range(3)]

    for i in range(9):  # iterate over rows
        for j in range(9):  # iterate over columns
            element = board[i][j]
            if element == 0:
                continue
            if (
                (element in rows[i])
                or (element in cols[j])
                or (element in block[i // 3][j // 3])
            ):
                return False
            rows[i].add(element)
            cols[j].add(element)
            block[i // 3][j // 3].add(element)
    return True


def displaySudoku(board: list[list[int]]) -> str:
    """
    Display sudoku board in a readable format.

    Parameters
    ----------
    grid : list of list
        List of list where elements can be accessed by row [i] & column [j]

    Returns
    ---------
    sudoku : str
        Text-based grid where empty cells are represented by 0, each subgrid is seperated by | and each row is seperated by - and +

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
