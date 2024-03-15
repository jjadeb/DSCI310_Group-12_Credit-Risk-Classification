
# Use the Python image as the base image
FROM quay.io/jupyter/minimal-notebook:notebook-7.0.6

# Install the Python packages 
RUN conda install -y --channel conda-forge \
    scipy==1.12.0 \
    numpy==1.26.4 \
    scikit-learn==1.4.1.post1 \
    pandas==2.2.1 \
    matplotlib==3.8.3 \
    seaborn==0.13.2 \
    jupyterlab \
    make \
    pygraphviz==1.12 \
    python-graphviz==0.20.1 \
    tabulate==0.9.0 \
    ipython==8.22.2

RUN pip install \
    graphviz==0.20.1 \
    ucimlrepo==0.0.3 \
    click==8.1.7

# Specify the default command to run
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--no-browser", "--allow-root"]
