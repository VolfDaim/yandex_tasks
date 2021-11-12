def min_max_s(p: int):
    a, b, c = distribute(p)
    if not possible_tr(a, b, c):
        print(-1)
        return

    print(a, b, c)
    if p % 2 == 0:
        a = 2
    else:
        a = 1

    b = c = int((p - a) / 2)

    print(a, b, c)


def possible_tr(a: int, b: int, c: int) -> bool:
    if a + b > c and a + c > b and b + c > a:
        return True
    return False


def distribute(p: int):
    a = b = c = p // 3
    ost = p % 3
    if ost == 2:
        b = c = c + 1
    elif ost == 1:
        c += 1
    return a, b, c


p = int(input())
min_max_s(p)
