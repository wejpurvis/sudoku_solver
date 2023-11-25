"""
This script is the entry point for the Sudoku Solver package.
It utilizes the backtracking algorithm from backtracking.py alongside various utility functions from utils.py to solve sudoku puzzles.

Author: William Purvis
Created: 25/11/2023
Last updated: 25/11/2023
"""
import sys

import tkinter as tk
from tkinter import filedialog

from utils import parse_grid, displaySudoku
from backtracking import solveBacktrack


def select_file():
    """
    Use tkinter to open a file dialog and return the selected file path.

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
    Ask user whether they want to solve uploaded Sudoku.

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
    It prompts the user to select a file, reads the Sudoku puzzle from the file,
    and then solves the puzzle using a backtracking algorithm.
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
