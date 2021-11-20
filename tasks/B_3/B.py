a = set()
for item in input().split():
    if item in a:
        print('YES')
    else:
        a.add(item)
        print('NO')
