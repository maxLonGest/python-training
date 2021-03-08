p = int(input())
x = int(input())
y = int(input())
sumDeposit = x * 100 + y
sumDeposit += int(sumDeposit * p / 100)
print(sumDeposit // 100, sumDeposit % 100)
