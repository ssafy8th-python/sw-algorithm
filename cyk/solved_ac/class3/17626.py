n = int(input())
lst = [0]*(n+1)
lst[1] = 1

for i in range(2, n+1):
    x = 1
    minV = 4        # 최대 개수는 4 이하
    while (x ** 2) <= i:
        minV = min(minV, lst[i-(x**2)])
        x += 1
    lst[i] = minV + 1

print(lst[-1])
