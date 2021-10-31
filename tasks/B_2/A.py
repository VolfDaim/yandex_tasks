from collections import Counter

item = []
while True:
    a = int(input())
    if a == 0:
        break
    item.append(a)
item = Counter(item).most_common()

print(max(item, key=lambda x: x[0])[1])
