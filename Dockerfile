#  Miniconda base image
FROM continuumio/miniconda3:latest

# Set the working directory in the container
WORKDIR /usr/src/app

# Set specific Python version
RUN conda install -y python=3.8

# Install individual Python packages using Conda
RUN conda install -y \
    scipy=1.12.0 \
    numpy=1.26.4 \
    scikit-learn=1.4.1.post1 \
    pandas=2.2.1 \
    matplotlib=3.8.3 \
    seaborn=0.13.2 \
    && conda clean -afy

RUN conda run -n base pip install \
    jupyterlab \
    graphviz==0.20.1 \
    pygraphviz==1.9 \
    python-graphviz==0.20.1

# Copy the rest of the application's code 
COPY . .

