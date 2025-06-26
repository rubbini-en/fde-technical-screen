import pytest
from sort import sort

# Standard cases
@pytest.mark.parametrize("width, height, length, mass, expected", [
    (10, 10, 10, 5, "STANDARD"),  # small, light
    (100, 100, 99, 19.99, "STANDARD"),  # just below all thresholds
])
def test_standard(width, height, length, mass, expected):
    assert sort(width, height, length, mass) == expected

# Bulky only
@pytest.mark.parametrize("width, height, length, mass", [
    (150, 10, 10, 5),  # width at threshold
    (10, 150, 10, 5),  # height at threshold
    (10, 10, 150, 5),  # length at threshold
    (100, 100, 100, 5),  # volume at threshold
    (200, 1, 1, 5),  # width above threshold
])
def test_bulky_only(width, height, length, mass):
    assert sort(width, height, length, mass) == "SPECIAL"

# Heavy only
@pytest.mark.parametrize("width, height, length, mass", [
    (10, 10, 10, 20),  # mass at threshold
    (10, 10, 10, 25),  # mass above threshold
])
def test_heavy_only(width, height, length, mass):
    assert sort(width, height, length, mass) == "SPECIAL"

# Both bulky and heavy (rejected)
@pytest.mark.parametrize("width, height, length, mass", [
    (150, 10, 10, 20),  # both at threshold
    (200, 200, 200, 25),  # both above threshold
    (100, 100, 100, 20),  # volume at threshold, mass at threshold
])
def test_rejected(width, height, length, mass):
    assert sort(width, height, length, mass) == "REJECTED"

# Edge cases: invalid input
@pytest.mark.parametrize("width, height, length, mass", [
    (0, 10, 10, 5),
    (10, 0, 10, 5),
    (10, 10, 0, 5),
    (10, 10, 10, 0),
    (-1, 10, 10, 5),
    (10, -1, 10, 5),
    (10, 10, -1, 5),
    (10, 10, 10, -1),
    ("a", 10, 10, 5),
    (10, "b", 10, 5),
    (10, 10, "c", 5),
    (10, 10, 10, "d"),
])
def test_invalid_input(width, height, length, mass):
    with pytest.raises(ValueError):
        sort(width, height, length, mass) 