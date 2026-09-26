import numpy as np

# TODO 
def sobel_response(block: np.ndarray) -> tuple[float, float, float]:
    """Return gx, gy, and edge strength."""
    kernel_x = np.array([[-1, 0, 1],
                         [-2, 0, 2],
                         [-1, 0, 1]], dtype=np.float32)
    kernel_y = np.array([[-1, -2, -1],
                         [0, 0, 0],
                         [1, 2, 1]], dtype=np.float32)

    gx = float(np.sum(block * kernel_x))
    gy = float(np.sum(block * kernel_y))

    strength = float(np.sqrt(gx**2 + gy**2))
    return gx, gy, strength

problem_5_input = np.array([[20, 20, 200], [20, 20, 200], [20, 20, 200]], dtype=np.float32)

# TODO 
gx, gy, strength = sobel_response(problem_5_input)
assert gx == 720.0 and gy == 0.0
print("Problem 5 passed")