def bench(length: int, pos: list):
    l_id = 0
    center = length // 2
    if center in pos and length % 2 != 0:
        print(center)
    else:
        while center > pos[l_id]+1:
            l_id += 1

        if center <= pos[l_id]:
            l_id -= 1
        print(pos[l_id], pos[l_id + 1])


length, count = [int(x) for x in input().split()]
pos = [int(x) for x in input().split()]
bench(length, pos)
