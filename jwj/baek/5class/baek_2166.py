N = int(input())

x = []
y = []
for _ in range(N):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)

x.append(x[0])
y.append(y[0])

res1 = 0
res2 = 0
for i in range(N):
    res1 += x[i] * y[i+1]
    res2 += x[i+1] * y[i]

answer = round(abs(res1 - res2) / 2, 1)

print(answer)
