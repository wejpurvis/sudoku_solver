"""
This script is the entry point for the Sudoku Solver package.
It utilizes the backtracking algorithm with minimum remaining value (MRV) heuristics.
The algorithm is from the :code:`backtracking_mrv` module and various utility functions
from the :code:`utils` module are used to to solve sudoku puzzles. Usage:
:code:`src/main.py input.txt` where :code:`input.txt` is the path to the file
containing the sudoku puzzle to be solved.

| **Author:** William Purvis
| **Created:** 25/11/2023
| **Last updated:** 09/12/2023
"""

import sys
import os
import time
import numpy as np

import argparse

from utils import parse_grid, displaySudoku
import cython.bt_mrv as bt


def parse_arguments():
    """
    Parse command line arguments.

    Returns
    ----------
        args (argparse.Namespace): Parsed command line arguments.

    Raises
    ----------
    ValueError
        If more than 1 argument is passed on CL.
    """
    parser = argparse.ArgumentParser(description="wp289's Sudoku Solver")
    parser.add_argument("input_file", help="Input sudoku as a text file")
    args = parser.parse_args()

    # check only 1 input file is provided
    if len(vars(args)) != 1:
        raise ValueError(
            "Invalid number of arguments. Please only upload 1 sudoku file."
        )

    return args


def is_valid_file(filename):
    """
    Check if a given file is valid based on whether file exists and whether it is a
    text file (.txt).

    Parameters
    ----------
    filename (str): The path of the file to be checked.

    Raises
    ----------
    FileNotFoundError
        If the file does not exist.
    ValueError
        If the file format is not valid.

    """
    # Check if file exists
    if not os.path.exists(filename):
        raise FileNotFoundError(f"{filename} not found.")

    # Check if .txt
    valid_extension = ".txt"
    file_extension = os.path.splitext(filename)[1].lower()

    if file_extension != valid_extension:
        raise ValueError(
            f"{file_extension} files are not supported."
            f"Please upload a {valid_extension} file."
        )


def get_user_input():
    """
    | Prompt user to select whether they want to solve the uploaded sudoku.
    | :code:`Do you want to solve the uploaded sudoku? [y/n]:` is displayed to the user.
      If user enters :code:`y`, :code:`True` is returned.
      If user enters :code:`n`, :code:`False` is returned.

    Returns
    ----------
        bool
            True if the user wants to solve sudoku, False otherwise.
    """
    while True:
        response = input("Do you want to solve the uploaded sudoku? [y/n]: ").lower()

        if response in ["y", "n"]:
            break
        else:
            print("Invalid input. Please enter 'y' for yes or 'n' for no.")

    if response == "y":
        return True
    else:
        return False


def main():
    """
    Main function that handles the execution of the Sudoku solver program.

    It reads the input Sudoku file (given as a .txt file via the CL),solves
    the Sudoku puzzle using backtracking algorithm,and displays the solved
    Sudoku along with the time taken for solving.

    If the user chooses not to solve the Sudoku, the program exits.

    Raises
    ----------
        FileNotFoundError
            If the input Sudoku file is not found.
        ValueError
            If there is an error in the input Sudoku file.

    """
    try:
        input_sudoku_path = parse_arguments().input_file
        is_valid_file(input_sudoku_path)
        # Display success message
        with open(input_sudoku_path, "r") as f:
            input_sudoku = f.read()
        print(f"Uploaded sudoku:\n\n{input_sudoku}")
        if get_user_input():
            # Solve sudoku
            sudoku_board = parse_grid(input_sudoku)
            sudoku_arr = np.array(sudoku_board, dtype=np.intc)
            start_time = time.time()
            solved_sudoku_array = bt.solved_MRV(sudoku_arr, 0, 0)
            end_time = time.time()
            solved_sudoku = [list(row) for row in solved_sudoku_array]
            print(f"Solved sudoku:\n\n{displaySudoku(solved_sudoku)}")
            print(f"Solved in {(end_time - start_time):.4f} seconds.")
        else:
            # Exit program
            print("Exiting program...")
            sys.exit()
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
