T = int(input())


def dfs(person, status):
    global maxV

    if maxV >= status:
        return

    if person == N:
        if maxV < status:
            maxV = status
    else:
        for job in range(N):
            if not visited[job]:
                visited[job] = True
                dfs(person+1, status * arr[person][job])
                visited[job] = False


for test_case in range(1, T+1):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            arr[i][j] = arr[i][j] / 100

    # jobs
    visited = [False] * N

    maxV = 0

    dfs(0, 1)

    print(f'#{test_case}{round(maxV * 100, 6) : 6f}')
