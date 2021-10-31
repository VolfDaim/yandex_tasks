"""
1.A Interactor
"""


def final_result(task_code: int, interactor: int, checker: int) -> int:

    if interactor == 1:
        return checker
    if interactor == 6:
        return 0
    if interactor == 7:
        return 1

    if task_code != 0:
        if interactor == 4 or interactor == 0:
            return 3
    elif interactor == 0:
        return checker

    return interactor


print(final_result(int(input()), int(input()), int(input())))
