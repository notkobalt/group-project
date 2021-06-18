import json


def Sort(listing):
    n = len(listing)
    for i in range(n - 1):
        flag = 0
        for j in range(n - 1):
            if listing[j] > listing[j + 1]:
                tmp = listing[j]
                listing[j] = listing[j + 1]
                listing[j + 1] = tmp
                flag = 1
        if flag == 0:
            break
    return listing
