# 2839 설탕 배달
# 주소: https://www.acmicpc.net/problem/2839

n = int(input())

minv = 100000000
for i in range(n // 5, -1, -1):
    if (n - 5 * i) % 3 == 0:
        if minv > (i + (n - 5 * i) // 3):
            minv = (i + (n - 5 * i) // 3)

if minv == 100000000:
    minv = -1

print(minv)