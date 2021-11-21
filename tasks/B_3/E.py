m = int(input())
hum = [set(input()) for i in range(m)]

n = int(input())
nums = [input() for i in range(n)]

answer = ''
max = 0

for num in nums:
    n = 0
    for item in hum:
        a = set(num)
        if item | a == a:
            n += 1
    if n > max:
        answer = num
        max = n
    elif n == max:
        answer += ' ' + num

print('\n'.join(answer.split()))
