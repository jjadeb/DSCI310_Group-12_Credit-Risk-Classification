
# Use the Python image as the base image
FROM quay.io/jupyter/minimal-notebook:notebook-7.0.6

# Set the working directory to the Docker container
#WORKDIR /usr/src/app

# Install the Python packages directly
RUN conda install -y \
    scipy==1.12.0 \
    numpy==1.26.4 \
    scikit-learn==1.4.1.post1 \
    pandas==2.2.1 \
    matplotlib==3.8.3 \
    seaborn==0.13.2 \
    jupyterlab 

RUN conda install -y --channel conda-forge pygraphviz==1.12 python-graphviz==0.20.1

RUN pip install \
    graphviz==0.20.1 \
    ucimlrepo==0.0.3 \
    click==8.1.7


# Copy the rest of the application's code into the container
#COPY . .


