# authors: Shahrukh Islam Prithibi, Sophie Yang, Yovindu Don, Jade Bouchard
# date: 2024-04-07
#
# This script renames the column names to be more intuitive and then saves the
# cleaned data as well as creates and saves various exploratory visualizations
#
# Usage: python scripts/cleaning_and_eda.py data/german.csv img data/german_clean.csv



import pandas as pd
from ucimlrepo import fetch_ucirepo 
import click
import matplotlib.pyplot as plt
import seaborn as sns
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.column_histogram import *

@click.command()
@click.argument('input_data_path', type=str)
@click.argument('fig_output_folder', type=str)
@click.argument('clean_data_output', type=str)
def exploratory_data_analysis(input_data_path, fig_output_folder, clean_data_output):
    # Load the dataset
    file_path = f'{input_data_path}'
    df = pd.read_csv(file_path)
    
    # Column names 
    df.columns = ["Status", "Duration", "Credit history", 
                    "Purpose", "Credit amount", "Savings account", "Employement", 
                    "Rate", "Personal status", 
                    "Guarantors", "Residence", "Property", 
                    "Age", "Installment", "Housing", "Existing credits", 
                    "Job", "Liable people", 
                    "Telephone", "Foreign worker", "Credit risk"]

    
    # Histograms for numerical columns
    numerical_columns = df.select_dtypes(include=['int64', 'float64']).columns
    for column in numerical_columns:
        column_plot = column_histogram(10,4,df,column)
        column_plot.figure.savefig(f'{fig_output_folder}/{column}.png')
    
    # Correlation heatmap for numerical columns
    plt.figure(figsize=(10, 8))
    sns.heatmap(df[numerical_columns].corr(), annot=True, fmt=".2f", cmap='coolwarm')
    plt.title('Correlation heatmap of numerical columns')
    plt.savefig(f'{fig_output_folder}/heatmap.png')

    df.to_csv(clean_data_output)
    

if __name__ == '__main__':
    exploratory_data_analysis()

