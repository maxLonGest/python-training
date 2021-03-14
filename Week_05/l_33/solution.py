a = list(map(int, input().split()))
_min = min(a)
_max = max(a)
_minIndex = a.index(_min)
_maxIndex = a.index(_max)
a[_maxIndex], a[_minIndex] = a[_minIndex], a[_maxIndex]
print(*a)
