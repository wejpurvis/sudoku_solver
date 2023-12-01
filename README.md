# C1 Sudoku Solver Coursework

William Purvis

## Project description

This project is a Sudoku Solver built for the C1 coursework. It aims to implement an algorithm that can solve Sudoku puzzles efficiently. The solver will take an input puzzle and provide the solution as the output. The project is implemented in python and includes documentation on how to install, run, and use the solver.

## Table of Contents

## How to install & run project

A dockerfile is provided to run the project with all of it's dependencies (as defined in `environment.yml`).

To run the file in docker run the following commands:

```cmd
docker build -t sudoku_solver_image . # builds docker image

docker run -it --name sudoku_docker_1 -v "C:\path_to_folder_containing_input_files:/usr/src/app/data" sudoku_v1 src/main.py /usr/src/app/data/input.txt
```

Where `C:\path_to_folder_containing_input_files` is the path to the directory containing the sudokus you want to solve, and `input.txt` is the name of the specific sudoku file you want to solve.

## How to use project

From the root directory run: `src/main.py input.txt` where `input.txt` is the name of the specific sudoku file you want to solve.

Documentation for this project has already been generated using `sphinx`. To read the documentation run the `index.html` file using the following command in the root directory of the project:

```bash
# Windows
start "" "docs\_build\html\index.html"
# Mac
open docs/_build/html/index.html
# Linux
xdg-open docs/_build/html/index.html
```

Alternatively to generate documentation locally, navigate to the `docs` subdirectory and run `make html` to re-build the documentation.

### License

[MIT](license.txt)
