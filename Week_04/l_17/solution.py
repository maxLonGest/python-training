def phib(_n):
    if _n in (1, 2):
        return 1
    return phib(_n - 1) + phib(_n - 2)


n = int(input())
print(phib(n))
