import click
import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline 
from sklearn.model_selection import cross_val_score, cross_validate, train_test_split
from sklearn.pipeline import Pipeline, make_pipeline
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.data_preprocessing import *

@click.command()
@click.argument('clean_data', type=str)
@click.argument('output_data_folder', type=str)

def main(clean_data, output_data_folder):
    df = pd.read_csv(f'{clean_data}')
    
    # Identifying numeric and categorical columns
    numeric_features = ["Duration", "Credit amount", "Age", "Rate", "Existing credits", "Liable people"]
    categorical_features = ["Status", "Credit history", "Purpose", "Savings account", "Employement", 
                            "Personal status", "Guarantors", "Residence", "Property", "Installment", 
                            "Housing", "Job", "Telephone", "Foreign worker"]
    

    # Using data_preprocessing function found in src
    X_transformed, y, preprocessor = preprocess_data(df, numeric_features, categorical_features)
    
    # Shape
    X_transformed.shape
    
    column_names = (
        numeric_features  
        + preprocessor.named_transformers_["cat"].get_feature_names_out().tolist()
    )
    pd.DataFrame(column_names).to_csv(f'{output_data_folder}/column_names.csv',index = False)
    
    # Applying the preprocessing
    X_train, X_test, y_train, y_test = train_test_split(X_transformed, y, test_size=0.2, random_state=42)
    
    pd.DataFrame(X_train).to_csv(f'{output_data_folder}/x_train.csv', index = False)
    pd.DataFrame(X_test).to_csv(f'{output_data_folder}/x_test.csv', index = False)
    pd.DataFrame(y_train).to_csv(f'{output_data_folder}/y_train.csv', index = False)
    pd.DataFrame(y_test).to_csv(f'{output_data_folder}/y_test.csv', index = False)


if __name__ == '__main__':
    main()

