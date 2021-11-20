n = int(input())
a = []

for i in range(n):
    a.append([int(item) for item in input().split()])
p = 0

for item in a:
    p += 4
    if [item[0] - 1, item[1]] in a:
        p -= 1
    if [item[0] + 1, item[1]] in a:
        p -= 1
    if [item[0], item[1] - 1] in a:
        p -= 1
    if [item[0], item[1] + 1] in a:
        p -= 1

print(p)
