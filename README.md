<!-- omit in toc -->
# C1 Sudoku Solver Coursework

**Author**: William Purvis

<!-- omit in toc -->
## Table of Contents
- [Project description](#project-description)
- [How to install \& run project](#how-to-install--run-project)
  - [Installing and running with Docker](#installing-and-running-with-docker)
  - [Running locally](#running-locally)
- [How to use project](#how-to-use-project)
  - [Documentation](#documentation)
- [License](#license)
  - [A note on the use of generation tools](#a-note-on-the-use-of-generation-tools)

## Project description

This project solves sudoku puzzles using a backtracking algorithm with a minimum remaining values (MRV) heuristic.

I completed this project as part of the C1 research computing coursework for the 2023-2024 data intensive science (DIS) MPhil at the University of Cambridge.

## How to install & run project

The sudoku solver can either be installed and run within a docker container, or the repository can be run locally. To clone this repository run the following:

```txt
git clone git@gitlab.developers.cam.ac.uk:phy/data-intensive-science-mphil/c1_assessment/wp289.git
```

### Installing and running with Docker

A dockerfile is provided to run the project alongside all of it's dependencies (defined in `environment.yml`) in a docker container. To build the docker image from the provided dockerfile run the following commands after cloning the repository:

```bash
docker build -t sudoku_solver_image . # builds docker image
```

As the project requires command-line interactions, the docker container needs to be run in interactive mode. The default input is `hard_sudoku2.txt` which can be found in the `test/example_sudokus/` subdirectory. Running the following commang will solve `hard_sudoku2.txt` in the docker container:

```bash
docker run -it sudoku_solver_image # run docker container with default input
```

To specify a different input file, mount the volume containing the file and pass the file path:

```bash
docker run -it -v /path/to/local/files:/data sudoku_solver_image /data/input_file.txt
```

Replace `/path/to/local/files` with the path to your local directory containing the input files (e.g. `C:\sudoku_puzzles`), and  `input_file.txt` with the name of your input file.


### Running locally

To run the sudoku solver without docker, create a conda environment from the provided `environment.yml` file and activate it:

```bash
conda env create -f environment.yml # create env
conda activate c1_coursework_wp289  # activate env
```

Once the environment has been activated, to run the sudoku solver navigate to the root directory and run `python src/main.py input.txt` where `input.txt` is the text file containing the sudoku you want to solve.

## How to use project

As specified in the coursework instructions:

> The programme should be able to take as input an incomplete grid in the form of a text file with a 9x9 grid of numbers with zero representing unknown values and `|`,`+`,`-` separating cells.

The sudoku solver is sensitive to the format of the provided sudoku and the input file must have the same format as the puzzle below:

```txt
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
```

### Documentation

[Read documentation](https://phy-data-intensive-science-mphil-c1_assessment.gitlab.io/wp289
)

Documentation for this project has already been generated using `sphinx` in both HTML and PDF formats. A PDF of the documentation can be found under `./docs/_build/latex/sudokusolver.pdf`

To read the documentation in a browser run the `index.html` file using the following command in the root directory of the project:

```bash
# Windows
start "" "docs\_build\html\index.html"
# Mac
open docs/_build/html/index.html
# Linux
xdg-open docs/_build/html/index.html
```

Alternatively, to generate documentation locally, navigate to the `docs` subdirectory and run `make clean html` followed by `make html` to re-build the documentation.

## License

This project is licensed under the MIT license - see the [LICENSE](license.txt)
file for details.

### A note on the use of generation tools

GitHub copilot was used throughout the project as it is installed on my IDE (VS code). It's use was limited to auto-completing lines of code where it made sense to do so (i.e, it was not used to blindly implement functionality, simply to complete code and/or docstring sentences). Copilot was also used to help generate *model* sudoku boards in the test files for the backtracking and backtracking MRV modules. ChatGPT was used to help de-bug the `.tex` file of the write-up (as this is the first time I use LaTeX) with prompts such as:

- **Prompt**: "Why does this text not compile in Latex: "[...] The \texttt{solve_backtrack()} was used to [...]"
- **Prompt**: "How should I reference a lstlisting in latex?"
- **Prompt**: "How can I get the word count of a latex document?"
