# Use the Python image as the base image
FROM python:3.11

# Set the working directory to the Docker container
WORKDIR /usr/src/app

# Install the Python packages directly
RUN pip install --no-cache-dir \
    scipy==1.12.0 \
    numpy==1.26.4 \
    scikit-learn==1.4.1.post1 \
    pandas==2.2.1 \
    matplotlib==3.8.3 \
    seaborn==0.13.2 \
    jupyterlab \
    graphviz==0.20.1 \
    pygraphviz==1.9 \
    python-graphviz==0.20.1

# Copy the rest of the application's code into the container
COPY . .

# Specify the default command to run
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--no-browser", "--allow-root"]
