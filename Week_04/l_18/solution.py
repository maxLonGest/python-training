def c(_n, _k):
    if _k == 1:
        return _n
    if _n == _k or _k == 0:
        return 1
    return c(_n - 1, _k) + c(_n - 1, _k - 1)


n = int(input())
k = int(input())
print(c(n, k))
