import pytest
import sys
import os
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Run pytest tests/* to run all tests

# Import the count_classes function from the src folder
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.column_histogram import *
from tests.column_histogram_data import *

# Test cases

### Correct Usage

def test_normal_data():
    '''column is numeric, has all number values, standard width and height'''
    assert data_normal_plot.get_xaxis().label.get_text() == 'measure', 'column name should be the title on the x axis'
    assert data_normal_plot.get_yaxis().label.get_text() == 'Count', 'count should be the title on the y axis'
    assert data_normal_plot.title.get_text() == "Histogram of measure", 'Histogram of measure should be the title of the plot'
    assert data_normal_plot.patches[0].get_height() == 2, "first rectangle in hist should be 2 tall"
    assert data_normal_plot.patches[1].get_height() == 0, "second rectangle in hist should be 0 tall"
    assert data_normal_plot.patches[2].get_height() == 2, "third rectangle in hist should be 2 tall"
    assert data_normal_plot.patches[3].get_height() == 1, "fourth rectangle in hist should be 1 tall"
    assert data_normal_plot.figure.get_size_inches()[0] == 10, 'Width of figure should be 10'
    assert data_normal_plot.figure.get_size_inches()[1] == 4, 'Height of figure should be 4'

def test_data_one_col_plot():
    '''dataframe only has one column'''
    assert data_one_col_plot.get_xaxis().label.get_text() == 'measure', 'column name should be the title on the x axis'
    assert data_one_col_plot.get_yaxis().label.get_text() == 'Count', 'count should be the title on the y axis'
    assert data_one_col_plot.title.get_text() == "Histogram of measure", 'Histogram of measure should be the title of the plot'
    assert data_one_col_plot.patches[0].get_height() == 3, "first rectangle in hist should be 3 tall"
    assert data_one_col_plot.patches[1].get_height() == 0, "second rectangle in hist should be 0 tall"
    assert data_one_col_plot.patches[2].get_height() == 1, "third rectangle in hist should be 1 tall"
    assert data_one_col_plot.patches[3].get_height() == 1, "fourth rectangle in hist should be 1 tall"
    assert data_one_col_plot.figure.get_size_inches()[0] == 10, 'Width of figure should be 10'
    assert data_one_col_plot.figure.get_size_inches()[1] == 4, 'Height of figure should be 4'    

def test_data_some_nan_plot():
    '''dataframe column is numeric and has some nan values'''
    assert data_some_nan_plot.get_xaxis().label.get_text() == 'measure', 'column name should be the title on the x axis'
    assert data_some_nan_plot.get_yaxis().label.get_text() == 'Count', 'count should be the title on the y axis'
    assert data_some_nan_plot.title.get_text() == "Histogram of measure", 'Histogram of measure should be the title of the plot'
    assert data_some_nan_plot.patches[0].get_height() == 2, "first rectangle in hist should be 3 tall"
    assert data_some_nan_plot.patches[1].get_height() == 1, "second rectangle in hist should be 0 tall"
    assert data_some_nan_plot.patches[2].get_height() == 1, "third rectangle in hist should be 1 tall"
    assert data_some_nan_plot.figure.get_size_inches()[0] == 10, 'Width of figure should be 10'
    assert data_some_nan_plot.figure.get_size_inches()[1] == 4, 'Height of figure should be 4'  


def test_data_decimals_included_plot():
    '''dataframe column has decimal values'''
    assert data_decimals_included_plot.get_xaxis().label.get_text() == 'measure', 'column name should be the title on the x axis'
    assert data_decimals_included_plot.get_yaxis().label.get_text() == 'Count', 'count should be the title on the y axis'
    assert data_decimals_included_plot.title.get_text() == "Histogram of measure", 'Histogram of measure should be the title of the plot'
    assert data_decimals_included_plot.patches[0].get_height() == 4, "first rectangle in hist should be 4 tall"
    assert data_decimals_included_plot.patches[8].get_height() == 1, "eighth rectangle in hist should be 1 tall"
    assert data_decimals_included_plot.figure.get_size_inches()[0] == 10, 'Width of figure should be 10'
    assert data_decimals_included_plot.figure.get_size_inches()[1] == 4, 'Height of figure should be 4'

def test_diff_width_val_plot():
    '''function call has different width value'''
    assert diff_width_val_plot.get_xaxis().label.get_text() == 'measure', 'column name should be the title on the x axis'
    assert diff_width_val_plot.get_yaxis().label.get_text() == 'Count', 'count should be the title on the y axis'
    assert diff_width_val_plot.title.get_text() == "Histogram of measure", 'Histogram of measure should be the title of the plot'
    assert diff_width_val_plot.patches[0].get_height() == 2, "first rectangle in hist should be 2 tall"
    assert diff_width_val_plot.patches[1].get_height() == 0, "second rectangle in hist should be 0 tall"
    assert diff_width_val_plot.patches[2].get_height() == 2, "third rectangle in hist should be 2 tall"
    assert diff_width_val_plot.patches[3].get_height() == 1, "fourth rectangle in hist should be 1 tall"
    assert diff_width_val_plot.figure.get_size_inches()[0] == 2, 'Width of figure should be 2'
    assert diff_width_val_plot.figure.get_size_inches()[1] == 4, 'Height of figure should be 4'

def test_low_width_val_plot():
    '''width value given is low'''
    assert low_width_val_plot.get_xaxis().label.get_text() == 'measure', 'column name should be the title on the x axis'
    assert low_width_val_plot.get_yaxis().label.get_text() == 'Count', 'count should be the title on the y axis'
    assert low_width_val_plot.title.get_text() == "Histogram of measure", 'Histogram of measure should be the title of the plot'
    assert low_width_val_plot.patches[0].get_height() == 2, "first rectangle in hist should be 2 tall"
    assert low_width_val_plot.patches[1].get_height() == 0, "second rectangle in hist should be 0 tall"
    assert low_width_val_plot.patches[2].get_height() == 2, "third rectangle in hist should be 2 tall"
    assert low_width_val_plot.patches[3].get_height() == 1, "fourth rectangle in hist should be 1 tall"
    assert low_width_val_plot.figure.get_size_inches()[0] == 1, 'Width of figure should be 1'
    assert low_width_val_plot.figure.get_size_inches()[1] == 4, 'Height of figure should be 4'

def test_diff_height_val_plot():
    '''function call has different hieght value'''
    assert diff_height_val_plot.get_xaxis().label.get_text() == 'measure', 'column name should be the title on the x axis'
    assert diff_height_val_plot.get_yaxis().label.get_text() == 'Count', 'count should be the title on the y axis'
    assert diff_height_val_plot.title.get_text() == "Histogram of measure", 'Histogram of measure should be the title of the plot'
    assert diff_height_val_plot.patches[0].get_height() == 2, "first rectangle in hist should be 2 tall"
    assert diff_height_val_plot.patches[1].get_height() == 0, "second rectangle in hist should be 0 tall"
    assert diff_height_val_plot.patches[2].get_height() == 2, "third rectangle in hist should be 2 tall"
    assert diff_height_val_plot.patches[3].get_height() == 1, "fourth rectangle in hist should be 1 tall"
    assert diff_height_val_plot.figure.get_size_inches()[0] == 10, 'Width of figure should be 2'
    assert diff_height_val_plot.figure.get_size_inches()[1] == 7, 'Height of figure should be 4'

def test_low_hieght_val_plot():
    '''hieght value given is low'''
    assert low_height_val_plot.get_xaxis().label.get_text() == 'measure', 'column name should be the title on the x axis'
    assert low_height_val_plot.get_yaxis().label.get_text() == 'Count', 'count should be the title on the y axis'
    assert low_height_val_plot.title.get_text() == "Histogram of measure", 'Histogram of measure should be the title of the plot'
    assert low_height_val_plot.patches[0].get_height() == 2, "first rectangle in hist should be 2 tall"
    assert low_height_val_plot.patches[1].get_height() == 0, "second rectangle in hist should be 0 tall"
    assert low_height_val_plot.patches[2].get_height() == 2, "third rectangle in hist should be 2 tall"
    assert low_height_val_plot.patches[3].get_height() == 1, "fourth rectangle in hist should be 1 tall"
    assert low_height_val_plot.figure.get_size_inches()[0] == 10, 'Width of figure should be 10'
    assert low_height_val_plot.figure.get_size_inches()[1] == 1, 'Height of figure should be 1'

def test_data_diff_col_name_plot():
    '''column name is different'''
    assert data_diff_col_name_plot.get_xaxis().label.get_text() == 'measure_b', 'column name should be the title on the x axis'
    assert data_diff_col_name_plot.get_yaxis().label.get_text() == 'Count', 'count should be the title on the y axis'
    assert data_diff_col_name_plot.title.get_text() == "Histogram of measure_b", 'Histogram of measure should be the title of the plot'
    assert data_diff_col_name_plot.patches[0].get_height() == 2, "first rectangle in hist should be 2 tall"
    assert data_diff_col_name_plot.patches[1].get_height() == 0, "second rectangle in hist should be 0 tall"
    assert data_diff_col_name_plot.patches[2].get_height() == 2, "third rectangle in hist should be 2 tall"
    assert data_diff_col_name_plot.patches[3].get_height() == 1, "fourth rectangle in hist should be 1 tall"
    assert data_diff_col_name_plot.figure.get_size_inches()[0] == 10, 'Width of figure should be 10'
    assert data_diff_col_name_plot.figure.get_size_inches()[1] == 4, 'Height of figure should be 4'


### Incorrect usage

def test_empty_dataframe():
    '''Empty dataframe passed to function'''
    with pytest.raises(EmptyDataFrameError, match='DataFrame must contain a column with numeric values'):
        column_histogram(10,4, data_empty, 'measure')

def test_empty_columns():
    '''Dataframe columns are empty'''
    with pytest.raises(EmptyDataFrameError, match='DataFrame must contain a column with numeric values'):
        column_histogram(10,4, data_empty_column, 'measure')
#####
def test_all_string_column_values():
    '''column values are not numeric'''
    with pytest.raises(NumericColumnError, match='DataFrame column must be numeric'):
        column_histogram(10,4, data_all_str_char, 'measure')

def test_string_number_column_values():
    '''column values are not numeric'''
    with pytest.raises(NumericColumnError, match='DataFrame column must be numeric'):
        column_histogram(10,4, data_all_str_int, 'measure')

def test_some_string_number_column_values():
    '''column values are not numeric'''
    with pytest.raises(NumericColumnError, match='DataFrame column must be numeric'):
        column_histogram(10,4, data_some_str_int, 'measure')

def test_non_integer_height():
    '''non-integer height value'''
    with pytest.raises(TypeError, match='Width and height must be a non-zero integers'):
        column_histogram(10,4.5, data_normal, 'measure')

def test_non_integer_width():
    '''non-integer width value'''
    with pytest.raises(TypeError, match='Width and height must be a non-zero integers'):
        column_histogram(10.7,4, data_normal, 'measure')

def test_zero_height():
    '''zero height value'''
    with pytest.raises(TypeError, match='Width and height must be a non-zero integers'):
        column_histogram(10,0, data_normal, 'measure')

def test_zero_width():
    '''zero width value'''
    with pytest.raises(TypeError, match='Width and height must be a non-zero integers'):
        column_histogram(0,4, data_normal, 'measure')

def test_str_height():
    '''string height value'''
    with pytest.raises(TypeError, match='Width and height must be a non-zero integers'):
        column_histogram(10,"4", data_normal, 'measure')

def test_str_width():
    '''string width value'''
    with pytest.raises(TypeError, match='Width and height must be a non-zero integers'):
        column_histogram("10",4, data_normal, 'measure')

def test_column_str():
    '''column name is not a string'''
    with pytest.raises(TypeError, match='Column name must be of type string'):
        column_histogram(10,4, data_normal, 3247)

def test_column_not_present():
    '''column name is not a string'''
    with pytest.raises(KeyError, match='Column name must exist in the DataFrame'):
        column_histogram(10,4, data_normal, "pinnaple")

def test_data_type():
    '''data is not of type pandas.core.frame.DataFrame'''
    with pytest.raises(TypeError, match='DataFrame must be of type pandas.core.frame.DataFrame'):
        column_histogram(10,4, "hello world", "measure")

def test_data_all_nan():
    '''column values are not numeric'''
    with pytest.raises(NumericColumnError, match='DataFrame column must be numeric'):
        column_histogram(10,4, data_all_nan, 'measure')



plt.close('all')