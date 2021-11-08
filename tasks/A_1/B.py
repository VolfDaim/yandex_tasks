from math import sqrt


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


def figure(a: Point, b: Point, c: Point, d: Point):
    """

    :param a:
    :param b:
    :param c:
    :param d:
    :return:
    """
    points = [a, b, c, d]
    points = sorted(points, key=lambda point: point.x)
    if angle_len(points[0], points[1]) == angle_len(points[2], points[3]):
        return 'YES'

    return 'NO'

def angle_len(a: Point, b: Point):
    if b.x - a.x == 0:
        return sqrt((b.x - a.x) ** 2 + (b.y - a.y) ** 2)
    else:
        return (b.y - a.y) / (b.x - a.x), sqrt((b.x - a.x) ** 2 + (b.y - a.y) ** 2)


for i in range(int(input())):
    points = [int(x) for x in input().split()]
    a = Point(points[0], points[1])
    b = Point(points[2], points[3])
    c = Point(points[4], points[5])
    d = Point(points[6], points[7])
    print(figure(a, b, c, d))
