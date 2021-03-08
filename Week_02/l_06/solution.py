start = int(input())
end = int(input())
if end % (end - (start-1)) == 0:
    print('YES')
else:
    print('NO')
