
def dfs(depth, idx):
    global minV

    if depth == N // 2:
        start = 0
        link = 0
        for i in range(N):
            for j in range(i, N):
                if visited[i] and visited[j]:
                    start += soccer[i][j]
                    start += soccer[j][i]

                elif not visited[i] and not visited[j]:
                    link += soccer[i][j]
                    link += soccer[j][i]
        absV = abs(start-link)
        if minV > absV:
            minV = absV
    else:
        for i in range(idx, N):
            visited[i] = True
            dfs(depth+1, i+1)
            visited[i] = False
               
N = int(input())

soccer = [list(map(int, input().split())) for _ in range(N)]

visited = [False] * N

minV = 2000

dfs(0, 0)

print(minV)