import pytest


def check_situation(field: list) -> str:
    count_x = field.count(1)
    count_o = field.count(2)

    if count_x != count_o and count_x != count_o + 1:
        return 'NO'

    win_x = 0
    win_o = 0

    for i in range(3):
        if field[i * 3] == field[i * 3 + 1] == field[i * 3 + 2]:
            if field[i * 3] == 1:
                win_x = 1
            elif field[i * 3] == 2:
                win_o = 1

        if field[i] == field[3 + i] == field[6 + i]:
            if field[i] == 1:
                win_x = 1
            elif field[i] == 2:
                win_o = 1

    if field[0] == field[4] == field[8]:
        if field[0] == 1:
            win_x = 1
        elif field[0] == 2:
            win_o = 1

    if field[2] == field[4] == field[6]:
        if field[2] == 1:
            win_x = 1
        elif field[2] == 2:
            win_o = 1

    if win_x == 1 and win_o == 1:
        return 'NO'
    if win_x == 1 and count_x == count_o:
        return 'NO'
    if win_o == 1 and count_x > count_o:
        return 'NO'

    return 'YES'


def test_check_situation():
    assert check_situation([1, 1, 1, 1, 1, 1, 1, 1, 1]) == 'NO'
    assert check_situation([2, 1, 1, 1, 1, 2, 2, 2, 1]) == 'YES'
    assert check_situation([1, 1, 1, 2, 0, 2, 0, 0, 0]) == 'YES'
    assert check_situation([0, 0, 0, 0, 1, 0, 0, 0, 0]) == 'YES'
    assert check_situation([0, 0, 0, 1, 1, 1, 2, 2, 2]) == 'NO'
    assert check_situation([1, 0, 0, 0, 1, 2, 2, 2, 1]) == 'NO'
    assert check_situation([2, 0, 1, 0, 2, 1, 1, 1, 2]) == 'NO'
    assert check_situation([2, 2, 1, 2, 2, 1, 1, 1, 1]) == 'YES'


if __name__ == '__main__':
    field = []
    for i in range(3):
        field += [int(item) for item in input().split()]
    print(check_situation(field))
