import pandas as pd
import pytest
import sys
import os

# Import the param_grid function from the src folder
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.param_grid import *

#Test data
n_estimator_multiple = [100, 150, 200, 250, 300]
max_depth_multiple = [1, 5, 10, 15, 20]

n_estimator_single = [100]
max_depth_single = [1]

n_estimator_less = [100, 150]
max_depth_less = [1, 5]

n_estimator_empty = []
max_depth_empty = []

n_estimator_non_list_single = 100
max_depth_non_list_single = 1

n_estimator_non_list_multiple = 100, 150, 200, 250
max_depth_non_list_multiple = 1, 5, 10, 15

n_estimator_non_numeric = [100, 'a', 200, 250]
max_depth_non_numeric = [1, 5, '10', 15]

n_estimator_non_numeric_single = ['1']
max_depth_non_numeric_single = ['a']

n_estimator_non_numeric_beginning = ['10', 100, 200, 250]
max_depth_non_numeric_beginning = ['b', 1, 5, 10]

#Expected output
test_multiple_correct_data_same_length_output = {'n_estimators': [100, 150, 200, 250, 300], 'max_depth': [1, 5, 10, 15, 20]}
test_multiple_correct_data_n_estimators_more_output = {'n_estimators': [100, 150, 200, 250, 300], 'max_depth': [1, 5]}
test_multiple_correct_data_max_depth_more_output = {'n_estimators': [100, 150], 'max_depth': [1, 5, 10, 15, 20]}
test_case_single_entry_output = {'n_estimators': [100], 'max_depth': [1]}
test_single_n_estimators_output = {'n_estimators': [100], 'max_depth': [1, 5, 10, 15, 20]}
test_single_max_depth_output = {'n_estimators': [100, 150, 200, 250, 300], 'max_depth': [1]}


### Correct Cases
#Test for correct return type
def test_correct_return_type():
    'Return type is a dictionary'
    result = param_grid_for_grid_search(n_estimator_multiple, max_depth_multiple)
    assert isinstance(result, dict), "param_grid_for_grid_search should return a dictionary"

#Test for correct input and return type with multiple entries
def test_multiple_correct_data_same_length():
    'Both n_estimators_range and max_depth_range are lists and have correct numeric entries and are of the same length'
    result = param_grid_for_grid_search(n_estimator_multiple, max_depth_multiple)
    assert result == test_multiple_correct_data_same_length_output, "Output does not match expected output"

#Test for correct input and return type with n_estimators_range having more entries than max_depth_range
def test_multiple_correct_data_n_estimators_more():
    'Both n_estimators_range and max_depth_range are lists and has correct numeric entries and n_estimators_range has more entries'
    result = param_grid_for_grid_search(n_estimator_multiple, max_depth_less)
    assert result == test_multiple_correct_data_n_estimators_more_output, "n_estimator doesn't match expected more entry output"

#Test for correct input and return type with max_depth_range having more entries than n_estimators_range
def test_multiple_correct_data_max_depth_more():
    'Both n_estimators_range and max_depth_range are lists and has correct numeric entries and max_depth_range has more entries'
    result = param_grid_for_grid_search(n_estimator_less, max_depth_multiple)
    assert result == test_multiple_correct_data_max_depth_more_output, "max_depth doesn't match expected more entry output"

#Test edge case with single entry for each list
def test_case_single_entry():
    'Both n_estimators_range and max_depth_range have single entry  and has correct numeric entries'
    result = param_grid_for_grid_search(n_estimator_single, max_depth_single)
    assert result == test_case_single_entry_output, "Single input is failing"

#Test for single entry in list for n_estimators_range but multiple entries for max_depth_range
def test_single_n_estimators():
    'n_estimators_range has single entry and max_depth_range has multiple entries and has correct numeric entries'
    result = param_grid_for_grid_search(n_estimator_single, max_depth_multiple)
    assert result == test_single_n_estimators_output, "Single input for n_estimators is failing"


#Test for single entry in list for max_depth_range but multiple entries for n_estimators_range
def test_single_max_depth():
    'max_depth_range has single entry and n_estimators_range has multiple entries and has correct numeric entries'
    result = param_grid_for_grid_search(n_estimator_multiple, max_depth_single)
    assert result == test_single_max_depth_output , "Single input for max_depth is failing"

### Error Cases

#Test for empty list for n_estimators_range
def test_empty_n_estimators_range():
    'n_estimators_range is an empty list'
    with pytest.raises(ValueError, match= "n_estimators_range must be a non-empty list."):
        param_grid_for_grid_search(n_estimator_empty, max_depth_multiple)

#Test for empty list for max_depth_range
def test_empty_max_depth_range():
    'max_depth_range is an empty list'
    with pytest.raises(ValueError, match= "max_depth_range must be a non-empty list"):
        param_grid_for_grid_search(n_estimator_multiple, max_depth_empty)

#Test non-list entry for n_estimators_range for single entry
def test_non_list_n_estimators_range_single_entry():
    'n_estimators_range is not a list and a single entry'
    with pytest.raises(TypeError, match= "n_estimators_range must be a list."):
        param_grid_for_grid_search(n_estimator_non_list_single, max_depth_multiple)

#Test non-list entry for n_estimators_range for multiple entry
def test_non_list_n_estimators_range():
    'n_estimators_range is not a list with multiple entries'
    with pytest.raises(TypeError, match= "n_estimators_range must be a list."):
        param_grid_for_grid_search(n_estimator_non_list_multiple, max_depth_multiple)

#Test non-list entry for max_depth_range for single entry
def test_non_list_max_depth_range_single_entry():
    'max_depth_range is not a list and a single entry'
    with pytest.raises(TypeError, match= "max_depth_range must be a list."):
        param_grid_for_grid_search(n_estimator_multiple, max_depth_non_list_single)

#Test non-list entry for max_depth_range for multiple entry
def test_non_list_max_depth_range():
    'max_depth_range is not a list with multiple entries'
    with pytest.raises(TypeError, match= "max_depth_range must be a list."):
        param_grid_for_grid_search(n_estimator_multiple, max_depth_non_list_multiple)

#Test for non-numeric entries in n_estimators_range
def test_non_numeric_n_estimators_range():
    'n_estimators_range has non-numeric entries'
    with pytest.raises(ValueError, match= "n_estimators_range must contain only numeric values."):
        param_grid_for_grid_search(n_estimator_non_numeric, max_depth_multiple)

#Test for non-numeric single entry in n_estimators_range
def test_non_numeric_single_n_estimators_range():
    'n_estimators_range has a single non-numeric entry'
    with pytest.raises(ValueError, match= "n_estimators_range must contain only numeric values."):
        param_grid_for_grid_search(n_estimator_non_numeric_single, max_depth_multiple)

#Test for non-numeric entries in n_estimators_range at beginning of list
def test_non_numeric_n_estimators_range_beginning():
    'n_estimators_range has non-numeric entries at the beginning'
    with pytest.raises(ValueError, match= "n_estimators_range must contain only numeric values."):
        param_grid_for_grid_search(n_estimator_non_numeric_beginning, max_depth_multiple)    

#Test for non-numeric entries in max_depth_range
def test_non_numeric_max_depth_range():
    'max_depth_range has non-numeric entries'
    with pytest.raises(ValueError, match= "max_depth_range must contain only numeric values."):
        param_grid_for_grid_search(n_estimator_multiple, max_depth_non_numeric)

#Test for non-numeric single entry in max_depth_range
def test_non_numeric_single_max_depth_range():
    'max_depth_range has a single non-numeric entry'
    with pytest.raises(ValueError, match= "max_depth_range must contain only numeric values."):
        param_grid_for_grid_search(n_estimator_multiple, max_depth_non_numeric_single)

#Test for non-numeric entries in max_depth_range at beginning of list
def test_non_numeric_max_depth_range_beginning():
    'max_depth_range has non-numeric entries at the beginning'
    with pytest.raises(ValueError, match= "max_depth_range must contain only numeric values."):
        param_grid_for_grid_search(n_estimator_multiple, max_depth_non_numeric_beginning)


