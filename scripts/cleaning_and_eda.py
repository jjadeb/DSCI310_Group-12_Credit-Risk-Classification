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

from pycredits import preprocess_data, column_histogram, map_labels_to_binary, param_grid_for_grid_search

@click.command()
@click.argument('input_data_path', type=str)
@click.argument('fig_output_folder', type=str)
@click.argument('clean_data_output', type=str)
def exploratory_data_analysis(input_data_path, fig_output_folder, clean_data_output):
    # Load the dataset
    file_path = f'{input_data_path}'
    df = pd.read_csv(file_path)
    
    # Column names 
    df.columns = ["Status", "Duration", "Credit_history", 
                    "Purpose", "Credit_amount", "Savings_account", "Employement", 
                    "Rate", "Personal_status", 
                    "Guarantors", "Residence", "Property", 
                    "Age", "Installment", "Housing", "Existing_credits", 
                    "Job", "Liable_people", 
                    "Telephone", "Foreign_worker", "Credit_risk"]

    
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

