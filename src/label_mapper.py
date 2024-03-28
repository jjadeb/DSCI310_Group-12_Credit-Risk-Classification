import numpy as np
import pandas as pd

import numpy as np

def map_labels_to_binary(y):
    """
    Transforms an array values by converting 1s to 0s and 2s to 1s 

    Parameters:
    ----------
    y : numpy.ndarray
        An array containing the label values. Expected values are 1 or 2.

    Returns:
    -------
    numpy.ndarray
        An array where all original values of 1 are replaced with 0 and all original values of 2 are replaced with 1.

    Raises:
    ------
    ValueError
        If the input array contains any values other than 1 or 2.

    Examples:
    --------
    >>> import numpy as np
    >>> y = np.array([1, 2, 1, 2, 2])
    >>> map_labels_to_binary(y)
    array([0, 1, 0, 1, 1])

    """
    if not np.all(np.isin(y, [1, 2])):
        raise ValueError("Input array contains invalid values. Only 1s and 2s are accepted.")
    y_mapped = y.copy()
    y_mapped[y_mapped == 1] = 0
    y_mapped[y_mapped == 2] = 1
    return y_mapped
