import collections

c = collections.Counter()
for item in input().split():
    c[item] += 1
print(' '.join(list(item for item in c.elements() if c[item] == 1)))
