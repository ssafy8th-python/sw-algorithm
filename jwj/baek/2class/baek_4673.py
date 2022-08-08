lst = [0] * 10001

for num in range(1, 10001):
    sumV = num
    while num > 0:
        sumV += num % 10
        num //= 10

    if sumV > 10000:
        continue

    lst[sumV] = 1


for idx in range(1, 10001):
    if lst[idx] == 0:
        print(idx)

