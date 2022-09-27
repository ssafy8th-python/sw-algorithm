T = int(input())


def dfs(row, status):
    global result

    if result <= status:
        return

    if row == N:
        if result > status:
            result = status
    else:
        for col in range(N):
            if not visited[col]:
                visited[col] = True
                dfs(row+1, status + arr[row][col])
                visited[col] = False


for test_case in range(1, T+1):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]

    # 공장 방문 여부
    visited = [False] * N

    result = 15000

    dfs(0, 0)

    print(f'#{test_case} {result}')