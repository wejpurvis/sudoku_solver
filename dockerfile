# Use basic miniconda image
FROM continuumio/miniconda3

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . /usr/src/app

# Create conda env from environment.yml
RUN conda env create -f environment.yml

# Activate conda activation to .bashrc
RUN echo "conda activate c1_coursework_wp289" >> ~/.bashrc

# Change shell to bash with login
SHELL ["/bin/bash","--login", "-c"]

# Compile Cython code
RUN apt-get update && apt-get install -y build-essential
RUN conda install cython
RUN cd src/cython && python setup.py build_ext --inplace


# Run the application with the conda environment activated
ENTRYPOINT ["conda", "run", "--no-capture-output", "-n", "c1_coursework_wp289", "python", "src/main.py"]

# Default to hard_sudoku2.txt as input
CMD ["test/example_sudokus/hard_sudoku2.txt"]
