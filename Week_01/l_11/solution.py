minute = int(input())
day = minute // 1440
minute = minute - day * 1440
hour = minute // 60
minute = minute % 60
print(hour, minute)
