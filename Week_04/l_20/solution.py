def reverse():
    _n = int(input())
    if _n != 0:
        reverse()
    print(_n)


reverse()
