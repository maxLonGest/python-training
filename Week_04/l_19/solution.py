def sumSequence():
    _n = int(input())
    if _n != 0:
        return _n + sumSequence()
    return _n


print(sumSequence())
