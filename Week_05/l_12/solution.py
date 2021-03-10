def palindrome(_n):
    return str(_n) == str(_n)[:: -1]


a = int(input())
b = int(input())
for i in range(a, b + 1):
    if palindrome(i):
        print(i)
