n = int(input())
end = n % 10
if end == 1 and n != 11:
    print(n, 'korova')
elif 10 <= n <= 20:
    print(n, 'korov')
elif end == 0 or end == 5 or end == 6 or end == 7 or end == 8 or end == 9:
    print(n, 'korov')
else:
    print(n, 'korovy')
