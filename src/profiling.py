"""
Profiling backtracking versus backtracking with MRV heuristics on 10, 000 sudoku boards
"""

import pickle
import time
import numpy as np
from backtracking import solveBacktrack
from backtracking2 import solve_backtrack_MRV
from pathlib import Path
from tqdm import tqdm


# Load 10k sudoku boards
spath = Path(__file__).parent.parent / "test/example_sudokus/tenk_sudoku_boards.pkl"

with open(spath, "rb") as f:
    loaded_boards = pickle.load(f)

# Run backtracking algorithm on 10k sudoku boards
time_to_solve_backtrack = []
for board in tqdm(loaded_boards):
    start_time = time.time()
    solveBacktrack(board, 0, 0)
    end_time = time.time()
    time_to_solve_backtrack.append(end_time - start_time)

# Run backtracking algorithm with MRV heuristics on 10k sudoku boards
time_to_solve_backtrack_MRV = []
for board in tqdm(loaded_boards):
    start_time = time.time()
    solve_backtrack_MRV(board, 0, 0)
    end_time = time.time()
    time_to_solve_backtrack_MRV.append(end_time - start_time)

# Print results
print("Average time to solve sudoku with backtracking:")
print(f"{np.mean(time_to_solve_backtrack):.6f} seconds")
print(f"Standard deviation: {np.std(time_to_solve_backtrack):.6f} seconds")

print("Average time to solve sudoku with backtracking and MRV heuristics:")
print(f"{np.mean(time_to_solve_backtrack_MRV):.6f} seconds")

print(f"Standard deviation: {np.std(time_to_solve_backtrack_MRV):.6f} seconds")
