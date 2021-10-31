from math import sqrt


def point_and_triangle(d: int, x: int, y: int) -> int:
    """

    :param d: координата d для А(0,0), В(d,0), c(0,d)
    :param x: координата X на оси абсцисс
    :param y: координата Y на оси ординат
    :return: 0, если точка X лежит внутри или на стороне треугольника
             номер ближайшей вершины, если точка Х лежит вне тругольника
    """

    if C_B(d, x) >= y >= 0 and 0 <= x <= d:
        return 0

    dist_A = dist(0, 0, x, y)
    dist_B = dist(d, 0, x, y)
    dist_C = dist(0, d, x, y)

    minim = min(min(dist_A, dist_B), dist_C)
    if minim == dist_A:
        return 1
    elif minim == dist_B:
        return 2
    else:
        return 3


def C_B(d: int, x: int) -> int:
    """

    :param x: координата х, в которой необходимо узнать значение прямой
    :param d: координата
    :return: значение функции прямой y = d - x
    """
    return d - x


def dist(x1, y1, x2, y2):
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


#d = int(input())
#x, y = [int(x) for x in input().split()]
#print(point_and_triangle(d, x, y))
