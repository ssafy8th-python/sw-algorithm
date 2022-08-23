T = int(input())

def dfs(k, s):
    global result

    if result < s:
        return

    if k == N:
        if result > s:
            result = s
    else:
        for i in range(N):
            if not visited[i]:
                visited[i] = True
                dfs(k+1, s+lst[k][i])
                visited[i] = False


for tc in range(1, T+1):
    N = int(input())

    lst = [list(map(int, input().split())) for _ in range(N)]

    visited = [False] * N

    result = 100

    dfs(0, 0)

    print(f'#{tc} {result}')
