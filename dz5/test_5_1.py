import pytest
from dz5.dz5_1 import binary_search

@pytest.mark.parametrize


def test_binary_search():
    assert binary_search([], 42) is None
    assert binary_search([0], 0) == 0
    assert binary_search([0], 1) is None
    assert binary_search([-1, 0, 42], 0) == 1
    assert binary_search([-42, 0, 42], 42) == 2
    assert binary_search([-6, -5, -4, -3, -2, -1], -4) == 2
    assert binary_search([1, 2, 3, 4, 5, 6], 4) == 3
    assert binary_search([1, 2, 3, 4, 5, 6, 7], 4) == 3
    assert binary_search([1, 2, 3, 4, 5], 7) is None
    assert binary_search([1, 2, 3, 4, 5, 6], 7) is None
    assert binary_search([42, 42, 42, 42, 42], 42) == 0
    assert binary_search([-42, -42, -42, -42, -42], -42) == 0
    assert binary_search([42, 42, 42, 42, 43], 43) == 4
    assert binary_search([41, 42, 42, 42, 42], 41) == 0
    assert binary_search([-2, -2, -1, 0, 1, 2, 2, 2], -1) == 2
    assert binary_search([-2, -2, -1, 0, 1, 1, 2, 2], 1) == 4
