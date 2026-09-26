import numpy as np

# TODO 
def contrast_stretch(
    image: np.ndarray,
    in_min: float,
    in_max: float,
    out_min: float = 0.0,
    out_max: float = 255.0,
) -> np.ndarray:
    """Change image values from one range to another."""
    normalized = (image - in_min) / (in_max - in_min)
    scaled = normalized * (out_max - out_min) + out_min
    clipped = np.clip(scaled, out_min, out_max)
    return clipped.astype(np.float32)

problem_4_input = np.array([50, 100, 150], dtype=np.float32)

# TODO 
expected = np.array([0.0, 127.5, 255.0], dtype=np.float32)
np.testing.assert_allclose(contrast_stretch(problem_4_input, 50, 150), expected)
print("Problem 4 passed")