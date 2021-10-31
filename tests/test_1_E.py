import pytest
from tasks.B_1.E import point_and_triangle


def test_point_and_triangle():
    assert point_and_triangle(5, 1, 1) == 0
    assert point_and_triangle(3, -1, -1) == 1
    assert point_and_triangle(4, 4, 4) == 2
    assert point_and_triangle(4, 2, 2) == 0
    #assert point_and_triangle(4, -4, 4) == 1
    assert point_and_triangle(100, 0, 100) == 0
