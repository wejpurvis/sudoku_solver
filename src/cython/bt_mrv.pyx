# cython: language_level=3
"""
This module is a cython implementation of backtracking_mrv.py. The functions are the
same with modified type declarations for performance. A cython struct is created to
hold the row and column indices of a cell. This is used to return a tuple of indices
from the find_empty_cell_mrv function.
"""
# Struct to hold row and column indices of a cell
ctypedef struct cell_position:
    int i
    int j

cpdef bint validate_cell(int[:, :] sudoku_board, int val, int i, int j):
    """
    Checks if given value is valid for cell[i][j] in sudoku_board.
    Validation is based on sudoku rules (each row must contain digits 1-9 without
    repetition, each column must contain digits 1-9 without repetition, and each of the
    nine 3 x 3 sub-grids must contain digits 1-9 wihtout repetition).

    Parameters
    -----------
    sudoku_board : int[:, :]
        two-dimensional c array representing sudoku board
    val : int
        Value to be checked
    i : int
        Row index of cell
    j : int
        Column index of cell

    Returns
    ---------
    boolean integer
        1 (True) if value is valid according to sudoku rules, 0 (False) otherwise
    """

    # Check row & column of val
    cdef int k
    for k in range(9):
        if sudoku_board[i][k] == val: # Check row
            return False
        if sudoku_board[k][j] == val: # Check column
            return False

    # Get index for block (9 blocks of 3x3)
    cdef int block_i = i // 3
    cdef int block_j = j // 3

    # Chek block of val
    cdef int b_i, b_j
    for b_i in range(block_i * 3, block_i * 3 + 3):
        for b_j in range(block_j * 3, block_j * 3 + 3):
            if sudoku_board[b_i][b_j] == val:
                return False
    return True


cpdef int n_poss_vals(int[:, :] sudoku_board, int i, int j):
    """
    Returns the number of possible values for a given cell in a Sudoku board.
    Uses :code:`validate_cell()` to check which numbers from 1 to 9 are valid for a
    given cell and returns the number of possible values for that cell.

    Parameters
    -----------
    sudoku_board : int[:, :]
        two-dimensional c array representing sudoku board
    i : int
        Row index of cell to be checked
    j : int
        Column index of cell to be checked

    Returns
    ----------
        int:
            Numbe of possible values for the given cell.
    """

    cdef int poss_vals = 0
    cdef int val
    for val in range(1, 10):
        if validate_cell(sudoku_board, val, i, j):
            poss_vals += 1
    return poss_vals



cpdef cell_position find_empty_cell_mrv(int[:, :] sudoku_board):
    """
    Iterates through given Sudoku board and uses n_possible_values to find the cell
    with the fewest possible values. Returns the row and column indices of that cell as
    a tuple to be used in the backtracking algorithm. This technique is called Minimum
    Remaining Values (MRV).

    Parameters
    -----------
    sudoku_board : int[:, :]
        two-dimensional c array representing sudoku board

    Returns
    ----------
    min_cell : cell_position struct
        Row and column indices of the cell with the fewest possible values.
    """

    cdef int min_poss_vals = 10
    cdef int poss_vals
    cdef int i, j
    # Initialise to invalid values (instead of None in python)
    cdef int min_i = -1
    cdef int min_j = -1

    for i in range(9):
        for j in range(9):
            if sudoku_board[i][j] == 0:
                poss_vals = n_poss_vals(sudoku_board, i, j)
                if poss_vals < min_poss_vals:
                    min_poss_vals = poss_vals
                    min_i = i
                    min_j = j

    # Use c struct to return python-type tuple
    cdef cell_position min_cell
    min_cell.i = min_i
    min_cell.j = min_j

    return min_cell

cpdef bint solve_backtrack_MRV(int[:, :] sudoku_board, int i, int j):
    """
    Recursive backtracking algorithm with MRV heuristic. Modifies sudoku_board in place
    and returns 1 (True) if a solution is found, 0 (False) otherwise.

    Parameters
    -----------
    sudoku_board : int[:, :]
        two-dimensional c array representing sudoku board
    i : int
        Row index of cell
    j : int
        Column index of cell

    Returns
    --------
    boolean integer
        1 (True) if sudoku board is solved, 0 (False) otherwise
    """

    # Find empty cell
    cdef cell_position empty_cell = find_empty_cell_mrv(sudoku_board)
    if empty_cell.i == -1 and empty_cell.j == -1: # No empty cells left: sudoku is solved
        return True
    else:
        i_e = empty_cell.i
        j_e = empty_cell.j

    # Try all possible values for empty cell (1-9)
    cdef int val
    for val in range(1,10):
        if validate_cell(sudoku_board, val, i_e, j_e):
            sudoku_board[i_e][j_e] = val
            if solve_backtrack_MRV(sudoku_board, i_e, j_e):
                return True
            sudoku_board[i_e][j_e] = 0 # Backtrack

    return False # Trigger recursive backtracking

cpdef int[:, :] solved_MRV(int[:, :] sudoku_board, int i, int j):
    """
    Wrapper function for solve_backtrack_MRV(). Returns solved sudoku board.

    Parameters
    -----------
    sudoku_board : int[:, :]
        two-dimensional c array representing sudoku board
    i : int
        Row index of cell
    j : int
        Column index of cell

    Returns
    --------
    int[:, :]
        Solved sudoku board

    Raises
    -------
    ValueError
        If sudoku board cannot be solved.
    """

    if solve_backtrack_MRV(sudoku_board, i, j):
        return sudoku_board
    else:
        raise ValueError('Sudoku puzzle cannot be solved.')
