from tasks.A_1.B import figure, Point


def test_figure():
    assert figure(Point(1, 1), Point(4, 2), Point(3, 0), Point(2, 3)) == 'YES'
    assert figure(Point(1, 1), Point(5, 2), Point(2, 3), Point(3, 0)) == 'NO'
    assert figure(Point(0, 0), Point(5, 1), Point(6, 3), Point(1, 2)) == 'YES'
    assert figure(Point(0, 0), Point(0, 5), Point(2, 0), Point(2, 5)) == 'YES'
    assert figure(Point(0, 0), Point(0, 5), Point(2, 0), Point(2, 5)) == 'YES'