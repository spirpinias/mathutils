import pytest
from mathutils import mean, median

def test_mean():
    assert mean([1, 2, 3, 4, 5]) == 3.0

def test_mean_empty():
    with pytest.raises(ValueError):
        mean([])

def test_median_odd():
    assert median([3, 1, 2]) == 2

def test_median_even():
    assert median([1, 2, 3, 4]) == 2.5