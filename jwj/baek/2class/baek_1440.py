time = list(map(int, input().split(":")))

hour = 0
for t in time:
    if 1 <= t <= 12:
        hour += 1

    if t >= 60:
        hour = 0
        break

if hour:
    print(hour * 2)

else:
    print(0)
