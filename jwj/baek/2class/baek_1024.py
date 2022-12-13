n, l = map(int, input().split())
t = 0
x = -1
iter = 0
for i in range(l, 101):
    t = (i * i - i) / 2
    # (n - t) // i >=0 음수에서 시작하면 안됨
    if (n - t) % i == 0 and (n - t) // i >= 0:
        # 시작 위치
        x = (n - t) // i
        # 길이
        iter = i
        break
if x == -1:
    print(-1)
else:
    for i in range(iter):
        print(int(x + i), end=" ")