import pytest
from calc import add


@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (-2, -2, -4),
    (2.5, 3.5, 6.0),
])
def test_add_various(a, b, expected):
    assert add(a, b) == expected
