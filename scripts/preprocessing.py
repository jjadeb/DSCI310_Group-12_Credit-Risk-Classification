import click
import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline 
from sklearn.model_selection import cross_val_score, cross_validate, train_test_split
from sklearn.pipeline import Pipeline, make_pipeline

@click.command()
@click.argument('raw_data', type=str)
@click.argument('output_data_folder', type=str)

def main(raw_data, output_data_folder):
    df = pd.read_csv(f'{raw_data}')
    
    # Splitting the dataset into attributes and target
    X = df.drop("Credit risk", axis=1)  
    y = df["Credit risk"]  # Target variable
    
    # Identifying numeric and categorical columns
    numeric_features = ["Duration", "Credit amount", "Age", "Rate", "Existing credits", "Liable people"]
    categorical_features = ["Status", "Credit history", "Purpose", "Savings account", "Employement", 
                            "Personal status", "Guarantors", "Residence", "Property", "Installment", 
                            "Housing", "Job", "Telephone", "Foreign worker"]
    
    # Creating transformers for numeric and categorical data
    numeric_transformer = StandardScaler()
    categorical_transformer = OneHotEncoder(handle_unknown='ignore')
    
    # Combining transformers into a ColumnTransformer
    preprocessor = ColumnTransformer(
        transformers=[
            ("num", numeric_transformer, numeric_features),
            ('cat', categorical_transformer, categorical_features)])
    
    # Applying the transformations
    X_transformed = preprocessor.fit_transform(X)
    
    # Shape
    X_transformed.shape
    
    column_names = (
        numeric_features  
        + preprocessor.named_transformers_["cat"].get_feature_names_out().tolist()
    )
    
    # Applying the preprocessing
    X_train, X_test, y_train, y_test = train_test_split(X_transformed, y, test_size=0.2, random_state=42)
    
    pd.DataFrame(X_train).to_csv(f'{output_data_folder}/x_train.csv', index = False)
    pd.DataFrame(X_test).to_csv(f'{output_data_folder}/x_test.csv', index = False)
    pd.DataFrame(y_train).to_csv(f'{output_data_folder}/y_train.csv', index = False)
    pd.DataFrame(y_test).to_csv(f'{output_data_folder}/y_test.csv', index = False)


if __name__ == '__main__':
    main()

