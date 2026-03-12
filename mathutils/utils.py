def clamp(value: float, min_val: float, max_val: float) -> float:
    """Clamp a value between a min and max."""
    return max(min_val, min(max_val, value))

def is_close(a: float, b: float, tolerance: float = 1e-9) -> bool:
    """Check if two floats are close enough to be considered equal."""
    return abs(a - b) <= tolerance