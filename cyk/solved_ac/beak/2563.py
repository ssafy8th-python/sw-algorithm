n = int(input())
arr = [[0]*101 for _ in range(101)]
for _ in range(n):
    x, y = map(int, input().split())
    for i in range(y, y+10):
        for j in range(x, x+10):
            arr[i][j] += 1
res = 0
for i in range(101):
    for j in range(101):
        if arr[i][j] != 0:
            res += 1
print(res)