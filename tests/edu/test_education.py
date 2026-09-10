import pytest


def add (a, b):
    return a + b

@pytest.mark.edu
def test_add():
    result = add(2, 3)
    assert result == 5

