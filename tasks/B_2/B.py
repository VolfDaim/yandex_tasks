def house_magazine(street: list):
    dist = 0
    left_magazine = -1
    right_magazine = len(street) - 1
    for item in enumerate(street):
        #print(item[0])
        if item[1] == 2:
            left_magazine = item[0]
            #print("\t", left_magazine)
        elif item[1] == 1:
            #print("\t", item[0])
            try:
                right_magazine = item[0] + street[item[0]::].index(2)
            except Exception as e:
                right_magazine = -1
            #print("\t", right_magazine)
            if left_magazine == -1:
                dist = max(dist, right_magazine - item[0])
            elif right_magazine == -1:
                dist = max(dist, item[0] - left_magazine)
            else:
                dist = max(min(item[0] - left_magazine, right_magazine - item[0]), dist)
            #print("\t", dist)
    return dist


street = [int(x) for x in input().split()]
print(house_magazine(street))
