import numpy as np
import pytest
import pandas as pd
from data_preprocessing import preprocess_data

numeric_features = ["Duration", "Credit amount", "Age", "Rate", "Existing credits", "Liable people"]
categorical_features = ["Status", "Credit history", "Purpose", "Savings account", "Employment",
                        "Personal status", "Guarantors", "Residence", "Property", "Installment",
                        "Housing", "Job", "Telephone", "Foreign worker"]

@pytest.fixture
def df():
    # Create a mock DataFrame with the expected structure
    data = {
        "Credit risk" : 1,
        "Duration": np.random.randint(1, 100, size=1000),
        "Credit amount": np.random.randint(100, 10000, size=1000),
        "Age": np.random.randint(18, 70, size=1000),
        "Rate": np.random.rand(1000),
        "Existing credits": np.random.randint(0, 10, size=1000),
        "Liable people": np.random.randint(0, 5, size=1000),
        **{feature: np.random.choice(['A', 'B', 'C'], size=1000) for feature in categorical_features}
    }
    return pd.DataFrame(data)

# Test 1: Check if column exists (Numeric Features)
def test_numeric_col_exists(df):
    expected_columns = set(numeric_features)
    assert expected_columns.issubset(df.columns)

# Test 2: Check if column exists (Categorical Features)
def test_categorical_col_exist(df):
    expected_columns = set(categorical_features)
    assert expected_columns.issubset(df.columns)

# Test 3: Check for nulls
def test_null_check_all_columns(df):
    for column in df.columns:
        assert df[column].isnull().sum() == 0
    
# Test 4: Check data type (Numerical Columns)
def test_numeric_columns_type(df):
    for column in numeric_features:
        assert df[column].dtype == int or df[column].dtype == np.int64 or df[column].dtype == np.float64 or df[column].dtype == float


# Test 5: Check data type and range between 0 and 1 (Categorical Columns)
def test_categorical_columns_type_and_range(df):
    for column in categorical_features:
        assert df[column].dtype == str or df[column].dtype == np.object_
        assert df[column].isin(['A', 'B', 'C']).all()

# Test 6: Test function for preprocess_data
def test_preprocess_data(df):
    numeric_features = ["Duration", "Credit amount", "Age", "Rate", "Existing credits", "Liable people"]
    categorical_features = ["Status", "Credit history", "Purpose", "Savings account", "Employment",
                            "Personal status", "Guarantors", "Residence", "Property", "Installment",
                            "Housing", "Job", "Telephone", "Foreign worker"]

    X_transformed, y = preprocess_data(df, numeric_features, categorical_features)

    assert isinstance(X_transformed, np.ndarray)
    assert isinstance(y, pd.Series)
    assert X_transformed.shape[0] == df.shape[0]
