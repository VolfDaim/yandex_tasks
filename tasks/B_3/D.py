string = ''
answer = set(range(1, int(input())+1))

while True:
    string = input()
    if string == 'HELP':
        break

    a = set(int(item) for item in string.split())
    if input() == 'YES':
        answer = answer & a
    else:
        answer -= a
print(*sorted(answer))
