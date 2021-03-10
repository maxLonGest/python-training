def isPositive(_a):
    return int(_a) > 0


def countPositeveInList(_list):
    count = 0
    for i in range(0, len(_list)):
        if isPositive(_list[i]):
            count += 1
    return count


a = list(input().split())
print(countPositeveInList(a))
