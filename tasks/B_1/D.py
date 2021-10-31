def build_school(id_student: list):
    #coord = [i for i in range(id_student[0], id_student[-1])]
    id = len(id_student)//2  # выбираем центр в качестве стартовой позиции
    return check_diff(id_student, id)


def check_diff(id_student: list, id: int) -> int:
    while True:
        if diff(id_student, id - 1, True) < 0:
            id -= 1
        elif diff(id_student, id + 1, False) < 0:
            id += 1
        else:
            return id_student[id]


def diff(id_student: list, id: int, checker: bool) -> int:
    """

    :param id_student: список координат домов учеников
    :param coord: координатная прямая от первого ученика до второго
    :param id: текущее положение школы
    :param checker: 1 - смещение влево, 0 - смещение вправо
    :return: изменение расстояния
    """
    result = 0
    diff_right = len(id_student[id:])
    diff_left = len(id_student[0:id])
    if checker:
        diff_left, diff_right = diff_right, diff_left

    result = diff_left - diff_right - 1
    return result


#print(build_school([0, 2, 5, 6, 10]))
#print(build_school([0, 1, 2, 4, 8, 9, 12]))
#print(build_school([-1, 0, 1]))
n = int(input())
a = [int(x) for x in input().split()]
print(build_school(a))
