def isAscending(_list):
    result = True
    if len(_list) == 1:
        return result
    else:
        i = 1
        while i != len(_list):
            result *= _list[i] > _list[i - 1]
            i += 1
    return result


a = list(map(int, input().split()))
if isAscending(a):
    print('YES')
else:
    print('NO')
