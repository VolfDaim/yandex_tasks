def count_seconds(count_diplom: list) -> int:
    max_sec = 0
    seconds = 0
    for item in count_diplom:
        seconds += item
        max_sec = max(max_sec, item)
    return seconds - max_sec


folder = int(input())
count_diplom = [int(x) for x in input().split()]
print(count_seconds(count_diplom))
