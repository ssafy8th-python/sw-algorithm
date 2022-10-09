# 경로 찾기
def dfs(init, start):
    global result

    if init == start:
        return

    for i in range(N):
        if result[start][i] == 1 and result[init][i] == 0:
            result[init][i] = 1
            dfs(init, i)

N = int(input())
result = [list(map(int, input().split())) for _ in range(N)]


for i in range(N):
    for j in range(N):
        if result[i][j] == 1:
            dfs(i, j)

for lst in result:
    print(*lst)