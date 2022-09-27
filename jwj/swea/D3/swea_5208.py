T = int(input())


def dfs(charge, station, cur, status):
    global minV

    if cur == N - 1:
        if minV > status:
            minV = status
        return

    if charge == 0 or minV <= status:
        return

    # 충전하지 않는 경우
    dfs(charge-1, station, cur+1, status)

    # 충전하는 경우
    if cur + 1 < N-1:
        dfs(station[cur+1], station, cur+1, status+1)


for test_case in range(1, T+1):
    arr = list(map(int, input().split()))
    N = len(arr)
    minV = 100
    dfs(arr[1], arr[1:], 0, 0)

    print(f'#{test_case} {minV}')
