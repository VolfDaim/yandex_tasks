def check_data(first: int, second: int):
    if first > 12 or second > 12 or first == second:
        return 1
    return 0


data = input().split()
print(check_data(int(data[0]), int(data[1])))
