n, m = [int(x) for x in input().split()]

body = [i for i in range(n)]

for i in range(m):
    j, k = [int(x) - 1 for x in input().split()]
    body[j], body[k] = body[k], body[j]

for i in range(n - 2):
    if body[i] != i:
        j = i
        while body[j] != i:
            body[j], body[n - 2] = body[n - 2], body[j]
            print(j + 1, n - 1)
            j = body[n - 2]

        body[j], body[n - 1] = body[n - 1], body[j]
        print(j + 1, n)
        j = body[n - 1]

        body[j], body[n - 1] = body[n - 1], body[j]
        print(j + 1, n)
        j = body[n - 1]

        print(body[n - 2] + 1, n - 1)
        body[body[n - 2]], body[n - 2] = body[n - 2], body[body[n - 2]]

if body[n - 1] != n - 1:
    body[n - 1], body[n - 2] = body[n - 2], body[n - 1]
    print(n - 1, n)
