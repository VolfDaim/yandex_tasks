from tasks.A_1.A import equation


def test_equation():
    assert equation(1, 1, 2, 2) == 'NO'
    assert equation(2, -4, 7, 1) == 2
    assert equation(35, 14, 11, -3) == 'NO'
    assert equation(0, 0, 1, 2) == 'INF'
    assert equation(2, 4, 1, 3) == -2
