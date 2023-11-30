# https://uwekorn.com/2021/03/01/deploying-conda-environments-in-docker-how-to-do-it-right.html
FROM continuumio/miniconda3

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . /usr/src/app

# Create the environment using the environment.yaml file
RUN conda env create -f environment.yml

# Make RUN commands use the new environment:
SHELL ["conda", "run", "-n", "c1_coursework_wp289", "/bin/bash", "-c"]

# Run the application
ENTRYPOINT ["conda", "run", "--no-capture-output", "-n", "c1_coursework_wp289", "python", "src/main.py"]
