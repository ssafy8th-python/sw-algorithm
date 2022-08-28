def dfs(depth, value):
    global maxV

    if depth <= N:
        if maxV < value:
            maxV = value
    
    for i in range(depth, N):
        n_depth = i+consultant[i][0]
        if n_depth <= N:
            dfs(n_depth, value + consultant[i][1])

N = int(input())

consultant = [list(map(int, input().split())) for _ in range(N)]

maxV = 0

dfs(0, 0)

print(maxV)