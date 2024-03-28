import numpy as np
from src.label_mapper import map_labels_to_binary

def test_map_labels_to_binary_all_zeros():
    y = np.array([1, 1, 1])
    y_mapped = map_labels_to_binary(y)
    assert np.array_equal(y_mapped, np.zeros(y.shape)), "All ones should be mapped to zeros"

def test_map_labels_to_binary_all_ones():
    y = np.array([2, 2, 2])
    y_mapped = map_labels_to_binary(y)
    assert np.array_equal(y_mapped, np.ones(y.shape)), "All twos should be mapped to ones"

def test_map_labels_to_binary_mixed():
    y = np.array([1, 2, 1, 2, 2])
    y_mapped = map_labels_to_binary(y)
    assert np.array_equal(y_mapped, np.array([0, 1, 0, 1, 1])), "Mixed should be mapped correctly"

def test_map_labels_to_binary_empty():
    y = np.array([])
    y_mapped = map_labels_to_binary(y)
    assert np.array_equal(y_mapped, np.array([])), "Empty array should return an empty array"

def test_map_labels_to_binary_invalid():
    y = np.array([0, 3, 4])
    try:
        y_mapped = map_labels_to_binary(y)
        assert False, "Expected an exception for invalid values"
    except ValueError:
        assert True
    except Exception as e:
        assert False, f"Unexpected exception type: {type(e)}"

def test_map_labels_to_binary_numpy_array():
    y = np.array([1, 2, 1, 2, 2], dtype=np.int32)
    y_mapped = map_labels_to_binary(y)
    expected_output = np.array([0, 1, 0, 1, 1], dtype=np.int32)
    assert np.array_equal(y_mapped, expected_output), "Function should handle numpy arrays"

def test_map_labels_to_binary_large_array():
    y = np.random.choice([1, 2], size=10000)
    y_mapped = map_labels_to_binary(y)
    assert len(y_mapped) == 10000, "Function should handle large arrays"
