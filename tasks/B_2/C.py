def palindrom(enter_string: str) -> int:
    center = len(enter_string) // 2
    str_left = enter_string[0:center]
    center += int(len(enter_string) % 2 != 0)
    str_right = reversed(enter_string[center:])
    return list(map(lambda x, y: x == y, str_left, str_right)).count(False)


print(palindrom(input()))
