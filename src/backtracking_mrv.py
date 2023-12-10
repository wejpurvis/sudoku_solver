"""
This module is an improved implementation of the backtracking algorithm in
backtracking.py. The :code:`validate_cell()` function is unchanged, but the
:code:`find_empty_cell()` and :code:`solve_backtrack()` functions have been modified to
include minimum remaining values (MRV) heuristics. This means that the backtracking
algorithm will always choose the cell with the fewest possible values to try first
(instead of the next empty cell). This is done using the :code:`n_possible_values()`
function.
"""


def validate_cell(sudoku_board: list[list[int]], val: int, i: int, j: int) -> bool:
    """
    Check if a value is valid for cell :code:`[i][j]` in :code:`sudoku_board`.
    Validity of sudoku is based off the following rules:


    1) Each row must contain the digits 1-9 without repetition.
    2) Each column must contain the digits 1-9 without repetition.
    3) Each of the nine 3 x 3 sub-grids
       must contain the digits 1-9 without repetition

    Parameters
    ------------
    sudoku_board : list[list[int]]
        List of lists representing the sudoku board
    val : int
        Value to be checked
    i : int
        Row index of cell
    j : int
        Column index of cell

    Returns
    ---------
    bool
        **True** if value is valid according to sudoku rules, **False** otherwise

    Raises
    ---------
    TypeError
        If sudoku board input is not a list of lists
    TypeError
        If value input is not an int
    TypeError
        If row/column indices are not ints
    ValueError
        If value input is not between 1-9
    ValueError
        If row/column indices are not between 0-8

    """
    # Check if board input is valid (list[list])
    if type(sudoku_board) != list:
        raise TypeError("Input must be a list")
    if type(sudoku_board[0]) != list:
        raise TypeError("Input must be a list of lists")

    # Check if value input is valid (int)
    if type(val) != int:
        raise TypeError("Value must be an int")
    if val < 1 or val > 9:
        raise ValueError("Value must be between 1-9")

    # Check if indices input (i & j) are valid (int)
    if type(i) != int:
        raise TypeError("Row index must be an int")
    if type(j) != int:
        raise TypeError("Column index must be an int")
    if i < 0 or i > 8:
        raise ValueError("Row index must be between 0-8")
    if j < 0 or j > 8:
        raise ValueError("Column index must be between 0-8")

    # Check row & column of val
    for k in range(9):
        if sudoku_board[i][k] == val:  # check row
            return False
        if sudoku_board[k][j] == val:  # check column
            return False

    # Get index for block (9 blocks of 3x3)
    block_i = i // 3
    block_j = j // 3

    # Check block of val
    for b_i in range(block_i * 3, block_i * 3 + 3):  # iterate over rows of block
        for b_j in range(block_j * 3, block_j * 3 + 3):  # iterate over cols of block
            if sudoku_board[b_i][b_j] == val:
                return False
    return True


def n_possible_values(sudoku_board: list[list[int]], i: int, j: int) -> int:
    """
    Returns the number of possible values for a given cell in a Sudoku board.
    Uses :code:`validate_cell()`.

    Parameters
    -----------
    sudoku_board : list[list[int]]
        List of lists representing sudoku board
    i : int
        Row index of cell to be checked
    j : int
        Column index of cell to be checked

    Returns
    ----------
        int:
            Number of possible values for the given cell (:code:`sudoku_board[i][j]`).
    """
    possible_values = 0
    for val in range(1, 10):
        if validate_cell(sudoku_board, val, i, j):
            possible_values += 1
    return possible_values


def find_empty_cell_MRV(sudoku_board: list[list[int]]) -> tuple[int, int]:
    """
    Iterates through given Sudoku board and uses :code:`n_possible_values()` to find
    the cell with the fewest possible values. Returns the row and column indices of
    that cell as a tuple to be used in the backtracking algorithm. This technique is
    called the Minimum Remaining Value (MRV) heuristic.

    Parameters
    -----------
    sudoku_board : list[list[int]]
        List of lists representing sudoku board

    Returns
    ----------
    min_cell : tuple[int, int]:
        Row and column indices of the cell with the fewest possible values.
    """
    # Initialize minimum possible values to 10
    # (always greater than 9, if cell can have all values between 1 and 9)
    min_possible_values = 10
    min_cell = None

    for i in range(9):
        for j in range(9):
            if sudoku_board[i][j] == 0:
                # Find number of possible values for given cell
                num_possible_vals = n_possible_values(sudoku_board, i, j)
                if num_possible_vals < min_possible_values:
                    # Update minimum possible values and cell
                    min_possible_values = num_possible_vals
                    min_cell = (i, j)

    # Return cell with fewest possible values (MRV)
    return min_cell


def solve_backtrack_MRV(sudoku_board, i, j) -> list[list[int]]:
    """
    **Backtracking algorithm with MRV**

    This function solves a Sudoku puzzle using the backtracking algorithm with Minimum
    Remaining Values (MRV) heuristic. It takes a Sudoku board represented as a 2D list
    (list of lists), along with the indices (i, j) of the current cell being considered.
    Returns the solved sudoku board as a 2D list of lists.

    Parameters
    -----------
    sudoku_board : (list[list[int]])
        List of list with dimensions 9x9 representing sudoku board
    i : int
        Row index of cell
    j : int
        Column index of cell

    Returns
    ---------
    list[list[int]]
        List of list with dimensions 9x9 representing solved sudoku board
    """

    # Find empty cell
    empty_cell = find_empty_cell_MRV(sudoku_board)
    if empty_cell is None:  # if no empty cells, sudoku is solved
        return sudoku_board
    else:
        i_e, j_e = empty_cell

    # Try values 1-9
    for val in range(1, 10):
        if validate_cell(sudoku_board, val, i_e, j_e):
            sudoku_board[i_e][j_e] = val
            result = solve_backtrack_MRV(sudoku_board, i_e, j_e)
            if result is not False:
                return result  # if sudoku is solved, passed solved grid up the stack
            else:
                sudoku_board[i_e][j_e] = 0  # backtrack

    return False  # trigger backtracking
