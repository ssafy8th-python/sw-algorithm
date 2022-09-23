T = int(input())


def f(start, cnt, s):
    global minV

    if minV < s:
        return

    if cnt == N:
        s = s + abs(values[start][0] - values[1][0]) + abs(values[start][1] - values[1][1])
        if minV > s:
            minV = s
    else:
        for i in range(N+2):
            if not visited[i]:
                visited[i] = True
                f(i, cnt+1, s + abs(values[start][0] - values[i][0]) + abs(values[start][1] - values[i][1]))
                visited[i] = False


for test_case in range(1, T+1):
    N = int(input())

    arr = list(map(int, input().split()))

    values = []

    visited = [False] * (N + 2)
    visited[0] = True
    visited[1] = True

    for idx in range(0, N * 2 + 4, 2):
        values.append((arr[idx], arr[idx+1]))
    minV = 1000
    f(0, 0, 0)

    print(f'#{test_case} {minV}')