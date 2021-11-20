import math
import pytest


def get_y(r, i, x0):
    if r < abs(i - x0):
        return 0
    return math.floor(math.sqrt(r ** 2 - (i - x0) ** 2))


def ceil(x0, y0, r, x1, y1, x2, y2):
    xl = max(x0 - r, x1)
    xr = min(x0 + r, x2)
    P = 0

    for i in range(xl, xr + 1):
        h2 = y0 + get_y(r, i, x0)
        h1 = y0 - get_y(r, i, x0)
        if h2 >= y1 and h1 <= y2:
            P += h2 - h1 + 1
            if h2 > y2:
                P -= h2 - y2
            if h1 < y1:
                P -= y1 - h1

    return P


"""def test_ceil():
    assert ceil(2, 2, 2, 0, 0, 5, 5) == 13
    assert ceil(2, 6, 2, 0, 0, 5, 5) == 4
    assert ceil(2, 6, 1, 0, 0, 5, 5) == 1
    assert ceil(2, 7, 1, 0, 0, 5, 5) == 0
    assert ceil(2, 2, 1, 0, 0, 5, 5) == 5
    assert ceil(7, 2, 2, 0, 0, 5, 5) == 1
    assert ceil(-2, 2, 2, 0, 0, 5, 5) == 1
    assert ceil(-2, -2, 3, 0, 0, 5, 5) == 1
    assert ceil(-1, -1, 2, -3, -3, 2, 2) == 13
"""

if __name__ == '__main__':
    x1, y1, x2, y2 = [int(item) for item in input().split()]
    x0, y0, r = [int(item) for item in input().split()]
    X1 = Y1 = X2 = Y2 = P = h = start = 0

    xa, ya = x0 - r, y0 + r  # левая верхняя точка круга
    xd, yd = x0 + r, y0 - r  # правая нижняя точка круга
    # print(xa, ya, xd, yd)

    if not (xa > x2 or xd < x1 or ya < y1 or yd > y2):  # если круг соприкасается с прямоугольником

        P = ceil(x0, y0, r, x1, y1, x2, y2)
    print(P)

