def IsPointInArea(_x, _y):
    return (
        (
            _y >= 2 * _x + 2 and
            _y >= -x and
            (_x + 1) ** 2 + (_y - 1) ** 2 <= 4
        ) or
        (
            _y <= 2 * _x + 2 and
            _y <= -_x and
            (_x + 1) ** 2 + (_y - 1) ** 2 >= 4
        )
    )


x = float(input())
y = float(input())
if IsPointInArea(x, y):
    print('YES')
else:
    print('NO')
