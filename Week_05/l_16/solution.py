def lastMaxInList(_list):
    maxList = _list[0]
    indexMax = 0
    for i in range(len(_list)):
        if _list[i] >= maxList:
            maxList = _list[i]
            indexMax = i
    return maxList, indexMax


a = list(map(int, input().split()))
print(*lastMaxInList(a))
