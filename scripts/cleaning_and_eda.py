import pandas as pd
from ucimlrepo import fetch_ucirepo 
import click
import matplotlib.pyplot as plt
import seaborn as sns

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

    # look at unique values in data
    {column: df[column].nunique() for column in df.columns}
    
    # look at describe table
    df.describe()
    
    # Histograms for numerical columns
    numerical_columns = df.select_dtypes(include=['int64', 'float64']).columns
    for column in numerical_columns:
        plt.figure(figsize=(10, 4))
        sns.histplot(df[column], kde=True)
        plt.title(f'Histogram of {column}')
        plt.savefig(f'{fig_output_folder}/{column}.png')
    
    # Correlation heatmap for numerical columns
    plt.figure(figsize=(10, 8))
    sns.heatmap(df[numerical_columns].corr(), annot=True, fmt=".2f", cmap='coolwarm')
    plt.title('Correlation heatmap of numerical columns')
    plt.savefig(f'{fig_output_folder}/heatmap.png')

    df.to_csv(clean_data_output)
    

if __name__ == '__main__':
    exploratory_data_analysis()

