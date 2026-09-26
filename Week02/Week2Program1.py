import numpy as np

# TODO 
def threshold_image(image: np.ndarray, threshold: int) -> np.ndarray:
    """Convert a grayscale image to black and white."""
    binary_img = np.where(image >= threshold, 255, 0)
    return binary_img.astype(np.uint8)

problem_1_input = np.array([[20, 128, 200], [100, 150, 250]], dtype=np.uint8)
problem_1_expected = np.array([[0, 255, 255], [0, 255, 255]], dtype=np.uint8)

# TODO 
np.testing.assert_array_equal(threshold_image(problem_1_input, 128), problem_1_expected)
print("Problem 1 passed")