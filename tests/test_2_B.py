from tasks.B_2.B import house_magazine


def test_max_dist():
    assert house_magazine([2, 0, 1, 1, 0, 1, 0, 2, 1, 2]) == 3
    assert house_magazine([0, 1, 0, 0, 0, 2, 1]) == 4
    assert house_magazine([1, 2, 0, 0, 0, 1, 0]) == 4
