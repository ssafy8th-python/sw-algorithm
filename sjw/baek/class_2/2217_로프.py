# 2217 로프
# 주소: https://www.acmicpc.net/problem/2217

n = int(input())
ropes = [int(input()) for _ in range(n)]

cnt = [0] * 10001
new = [0] * n

for j in ropes:
    cnt[j] += 1

for k in range(1, 10001):
    cnt[k] += cnt[k - 1]

for m in ropes[::-1]:
    cnt[m] -= 1
    new[cnt[m]] = m


maxw = 0
while n > 0:
    for i in new:
        if maxw < i * n:
            maxw = i * n
        n -= 1
print(maxw)