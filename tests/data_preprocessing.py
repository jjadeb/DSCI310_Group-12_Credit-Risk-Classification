from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer

def preprocess_data(df, numeric_features, categorical_features):
    """
    Preprocesses the input DataFrame by applying scaling to numeric features and one-hot encoding to categorical features.

    Parameters:
        df (pd.DataFrame): Input DataFrame.
        numeric_features (list): List of names of numeric features.
        categorical_features (list): List of names of categorical features.

    Returns:
        tuple: Tuple containing preprocessed features (X_transformed) and target variable (y).
    """
    # "Credit risk" is the target variable and is always dropped
    y = df["Credit risk"]
    X = df.drop("Credit risk", axis=1)
    
    numeric_transformer = StandardScaler()
    categorical_transformer = OneHotEncoder(handle_unknown='ignore')

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", numeric_transformer, numeric_features),
            ('cat', categorical_transformer, categorical_features)])

    X_transformed = preprocessor.fit_transform(X)
    
    return X_transformed, y
