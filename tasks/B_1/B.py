def path_to_home(n: int, i: int, j: int) -> int:
    if i > j:
        i, j = j, i

    return min(j - i, i + n - j)-1


task = input().split()

print(path_to_home(int(task[0]), int(task[1]), int(task[2])))
