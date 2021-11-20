n = int(input())
a = [int(item) for item in input().split()]

sum = 0
maximum = a[0]

for item in a:
    if item > maximum:
        maximum = item
    sum += item

if sum - maximum >= maximum:
    print(sum)
else:
    print(2 * maximum - sum)
