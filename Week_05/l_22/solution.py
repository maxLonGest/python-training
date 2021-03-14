def minOfPositive(_list):
    _min = 1001
    for i in range(len(_list)):
        if _min > _list[i] and _list[i] > 0:
            _min = _list[i]
    return _min


a = list(map(int, input().split()))
print(minOfPositive(a))
