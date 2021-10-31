from tasks.B_2.D import bench


def test_bench():
    assert bench(5, [0, 2]) == [2]
    assert bench(13, [1, 4, 8, 11]) == [4, 8]
    assert bench(14, [1, 6, 8, 11, 12, 13]) == [6, 8]
