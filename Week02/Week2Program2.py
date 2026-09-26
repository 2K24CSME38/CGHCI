# TODO 
def display_memory_bytes(width: int, height: int, bpp: int) -> int:
    """Return image memory in bytes."""
    total_bits = width * height * bpp
    total_bytes = total_bits // 8
    return total_bytes

# TODO 
expected_bytes = 1920 * 1080 * 24 // 8
assert display_memory_bytes(1920, 1080, 24) == expected_bytes
print("Problem 2 passed")