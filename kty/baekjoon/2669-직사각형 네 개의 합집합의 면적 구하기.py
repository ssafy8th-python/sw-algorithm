graph = [[0] * 101 for _ in range(101)]

for _ in range(4):
    c1, r1, c2, r2 = map(int, input().split())
    for row in range(r1, r2):
        for col in range(c1, c2):
            graph[row][col] += 1

cnt = 0
for i in range(101):
    for j in range(101):
        if graph[i][j] > 0:
            cnt += 1

print(cnt)