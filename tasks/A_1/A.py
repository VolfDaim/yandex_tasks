def equation(a: int, b: int, c: int, d: int):
    if b != 0 and d != 0 and a / b == c / d:
        return 'NO'
    if a == b == 0:
        return 'INF'
    elif a != 0 and b % a == 0:
        return int(-b / a)
    return 'NO'


a = int(input())
b = int(input())
c = int(input())
d = int(input())
print(equation(a, b, c, d))
