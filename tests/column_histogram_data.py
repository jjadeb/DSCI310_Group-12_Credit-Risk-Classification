
import sys
import os
import pandas as pd
import numpy as np

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.column_histogram import column_histogram

### Valid Cases

data_normal = pd.DataFrame({
        'year': np.array([1901, 1902, 1903, 1904, 1905]),
        'measure' : np.array([25, 25, 50, 50, 75]),
    })
data_normal_plot = column_histogram(10,4,data_normal,'measure')

data_one_col = pd.DataFrame({
        'measure': np.array([1902, 1902, 1902, 1903, 1904]),
    })
data_one_col_plot = column_histogram(10,4,data_one_col,'measure')

data_some_nan = pd.DataFrame({
        'year': np.array([1901, 1902, 1903, 1904, 1905, 1906]),
        'measure' : np.array([25, 25, 50, None, 100, None]),
    })
data_some_nan_plot = column_histogram(10,4,data_some_nan,'measure')

data_decimals_included = pd.DataFrame({
        'year': np.array([1901, 1902, 1903, 1904, 1905]),
        'measure': [0.1, 5, 0.6, 0.1, 0.4]
    })
data_decimals_included_plot = column_histogram(10,4,data_decimals_included,'measure')

diff_width_val_plot = column_histogram(2,4,data_normal,'measure')

diff_height_val_plot = column_histogram(10,7,data_normal,'measure')

low_width_val_plot = column_histogram(1,4,data_normal,'measure')

low_height_val_plot = column_histogram(10,1,data_normal,'measure')

data_diff_col_name = pd.DataFrame({
        'year': np.array([1901, 1902, 1903, 1904, 1905]),
        'measure' : np.array([25, 25, 50, 50, 100]),
        'measure_b': [25, 25, 50, 50, 75]
    })
data_diff_col_name_plot = column_histogram(10,4,data_diff_col_name,'measure_b')


### Invalid Cases

data_empty = pd.DataFrame()

data_empty_column = pd.DataFrame({
        'year': [],
        'measure' : [],
    })

data_not_numeric = pd.DataFrame({
        'measure' : np.array(["a","b","c","d","e"])
    })

data_all_str_char = pd.DataFrame({
        'measure' : np.array(["a","b","c","d","e"])
    })

data_all_str_int = pd.DataFrame({
        'measure' : np.array(["1","2","3","4","5"])
    })

data_some_str_int = pd.DataFrame({
        'measure' : np.array([1,"2",3,4,"5"])
    })

data_all_nan = pd.DataFrame({
        'year': np.array([1901, 1902, 1903, 1904, 1905, 1906]),
        'measure' : np.array([None, None, None, None, None, None]),
    })







