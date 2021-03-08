def power(_a, _n):
    _result = 1
    if _n == 0:
        _result = 1
    elif _n > 0:
        while _n >= 1:
            _result *= _a
            _n -= 1
    else:
        while _n <= -1:
            _result /= _a
            _n += 1
    return _result


a = float(input())
n = int(input())
print(power(a, n))
