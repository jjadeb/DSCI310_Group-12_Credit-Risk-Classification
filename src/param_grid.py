import numpy as np
import pandas as pd
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier


def param_grid_for_grid_search(n_estimators_range, max_depth_range):
    """
    Create parameter grid for grid search.

    Parameters:
    -----------
    n_estimators_range : list
        A list containing the range of values for the number of trees in the forest.

    max_depth_range : list
        A list containing the range of values for the maximum depth of the trees.

    Returns:
    --------
    dict
        A dictionary representing the parameter grid for grid search.

    Raises:
    -------
    TypeError
        If either `n_estimators_range` or `max_depth_range` is not provided as a list.
    
    ValueError
        If either `n_estimators_range` or `max_depth_range` is an empty list, or if any non-numeric values are included 
        in the parameter ranges.

    Example:
    --------
    n_estimators_range = [100, 150, 200, 250, 300]
    max_depth_range = [1, 5, 10, 15, 20]
    param_grid = param_grid_for_grid_search(n_estimators_range, max_depth_range)
    """
    
    param_grid = {
        'n_estimators': n_estimators_range, 
        'max_depth': max_depth_range
        }
    
    if not isinstance(param_grid, dict):
        raise TypeError("The function should return a dictionary.")
    
    if not n_estimators_range:
        raise ValueError("n_estimators_range must be a non-empty list.")
    if not max_depth_range:
        raise ValueError("max_depth_range must be a non-empty list.")
    
    if not isinstance(n_estimators_range, list):
        raise TypeError("n_estimators_range must be a list.")
    if not isinstance(max_depth_range, list):
        raise TypeError("max_depth_range must be a list.")

    if any(not isinstance(i, (int, float)) for i in n_estimators_range):
        raise ValueError("n_estimators_range must contain only numeric values.")
    if any(not isinstance(f, (int, float)) for f in max_depth_range):
        raise ValueError("max_depth_range must contain only numeric values.")
    
    return param_grid