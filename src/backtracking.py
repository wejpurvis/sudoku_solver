"""
This module contains the backtracking algorithm for solving sudoku puzzles.
The backtracking algorithm works recursively by trying values 1-9 in empty
cells and 'backtracking' if the value is invalid.
Validity of values is checked using ``validateCell()``, which checks
if the value is valid for the cell according to sudoku rules.

**References:**

- `Norvig, P. (2013). Solving Every Sudoku Puzzle <https://norvig.com/sudoku.html>`_
- `GeeksforGeeks (2020). Sudoku | Backtracking-7 \
   <https://www.geeksforgeeks.org/sudoku-backtracking-7>`_

"""


def validate_cell(sudoku_board: list[list[int]], val: int, i: int, j: int) -> bool:
    """
    Check if a value is valid for cell :code:`[i][j]` in :code:`sudoku_board`.
    Validity of sudoku is based off the following rules:


    1) Each row must contain the digits 1-9 without repetition.
    2) Each column must contain the digits 1-9 without repetition.
    3) Each of the nine 3 x 3 sub-boxes of the grid
       must contain the digits 1-9 without repetition

    Parameters
    ----------
    sudoku_board : list[list[int]]
        List of list representing sudoku board
    val : int
        Value to be checked
    i : int
        Row index of cell
    j : int
        Column index of cell

    Returns
    ---------
    bool
        True if value is valid according to sudoku rules, False otherwise

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


def find_empty_cell(sudoku_board: list[list[int]]) -> tuple[int, int]:
    """
    Find the first empty cell in :code:`sudoku_board` and return
    its row & column indices.

    Parameters
    ----------
    sudoku_board : list[list[int]]
        List of lists representing sudoku board

    Returns
    ---------
    tuple[int, int]
        Tuple containing row & column indices of empty cell or
        None if no empty cells are found

    """
    for i in range(9):
        for j in range(9):
            if sudoku_board[i][j] == 0:
                return (i, j)
    return None


def solve_backtrack(grid: list[list[int]], i: [int], j: [int]) -> list[list[int]]:
    """
    Solve sudoku using backtracking algorithm (recursive implementation).
    The algorithm works as follows:


    1) Find empty cell using findEmptyCell()
    2) If there are no empty cells, the sudoku is solved and
       the resulting grid is returned
    3) Try values 1-9
    4) Validate value using validateCell()
    5) Repeat steps 1-4 until sudoku is solved

    Parameters
    ----------
    grid : list[list[int]]
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
    empty_cell = find_empty_cell(grid)
    if empty_cell is None:  # if no empty cells, sudoku is solved
        return grid
    else:
        i_e, j_e = empty_cell

    # Try values 1-9
    for val in range(1, 10):
        if validate_cell(grid, val, i_e, j_e):
            grid[i_e][j_e] = val
            result = solve_backtrack(grid, i_e, j_e)
            if result is not False:
                return result  # if sudoku is solved, passed solved grid up the stack
            else:
                grid[i_e][j_e] = 0  # backtrack

    return False  # trigger backtracking
