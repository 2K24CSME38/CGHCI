import numpy as np

# TODO 
def mean_filter_3x3(neighborhood: np.ndarray) -> int:
    """Return the rounded average of 9 pixels."""
    total_sum = np.sum(neighborhood)
    avg_val = total_sum / 9.0
    return int(round(avg_val))

problem_3_input = np.array([[10, 20, 10], [30, 50, 30], [10, 20, 10]], dtype=np.uint8)

# TODO 
assert mean_filter_3x3(problem_3_input) == 21
print("Problem 3 passed")