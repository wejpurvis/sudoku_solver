"""
This script is the entry point for the Sudoku Solver package.
It utilizes the backtracking algorithm from the backtracking module alongside various utility functions from utils module to solve sudoku puzzles.
The user is prompted to select a file containing a sudoku puzzle, which is then solved and displayed to the user within the terminal.

**Author:** William Purvis \
**Created:** 25/11/2023 \
**Last updated:** 26/11/2023
"""


import sys
import os

import tkinter as tk
from tkinter import filedialog

from src.utils import parse_grid, displaySudoku
from src.backtracking import solveBacktrack

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


def select_file():
    """
    Use :code:`tkinter` library to open file explorer so that user can select a file. The file path of the selected file is returnes.

    Returns
    ----------
    str
        Path to the selected file.
    """
    root = tk.Tk()
    root.withdraw()

    # Open file dialog and return the selected file path
    file_path = filedialog.askopenfilename()
    return file_path


def get_user_input():
    """
    Prompt user to select whether they want to solve the uploaded sudoku. \
    :code:`Do you want to solve the uploaded sudoku? [y/n]:` is displayed to the user.
    If user enters :code:`y`, :code:`True` is returned. If user enters :code:`n`, :code:`False` is returned.

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
    It prompts the user to select a file, reads the Sudoku puzzle from the given file,
    and then solves the puzzle using a backtracking algorithm if the input file has the correct format.
    """
    file_path = select_file()
    if file_path:
        print(f"Selected file: {file_path}")
        with open(file_path, "r") as f:
            sudoku = f.read()

        print(f"Unsolved sudoku:\n\n{sudoku}")
        if get_user_input():
            # Solve sudoku
            sudoku_board = parse_grid(sudoku)
            solved_sudoku = solveBacktrack(sudoku_board, 0, 0)
            print(f"Solved sudoku:\n\n{displaySudoku(solved_sudoku)}")

        else:
            # Exit program
            sys.exit()
    else:
        print("No file was selected")


if __name__ == "__main__":
    main()
