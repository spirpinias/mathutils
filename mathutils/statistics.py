def mean(values: list[float]) -> float:
    if not values:
        raise ValueError("Cannot calculate mean of empty list")
    return sum(values) / len(values)

def median(values: list[float]) -> float:
    if not values:
        raise ValueError("Cannot calculate median of empty list")
    sorted_vals = sorted(values)
    n = len(sorted_vals)
    mid = n // 2
    return sorted_vals[mid] if n % 2 else (sorted_vals[mid - 1] + sorted_vals[mid]) / 2

def variance(values: list[float]) -> float:
    m = mean(values)
    return sum((x - m) ** 2 for x in values) / len(values)