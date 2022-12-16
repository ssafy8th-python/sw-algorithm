import sys
input = sys.stdin.readline

N = int(input())

city = [list(map(int, input().split())) for _ in range(N)]

INF = int(1e9)

dp = [[INF] * (1 << N) for _ in range(N)]


def dfs(cur, visited):
    # 최소 비용이 계산되어 있다면
    if dp[cur][visited] != INF and dp[cur][visited] != -1:
        return dp[cur][visited]

    if dp[cur][visited] == -1:
        return INF

    # 마지막 도시에서 0번째 도시로 이동 하는 값
    if visited == (1 << N) - 1:
        # 해당 도시로 가는 값이 존재하는 지
        if city[cur][0]:
            return city[cur][0]
        return INF

    for i in range(1, N):       # 모든 도시를 탐방

        if not city[cur][i]:    # 가는 경로가 없다면
            continue

        if visited & (1 << i):  # 이미 방문한 도시라면
            continue

        dp[cur][visited] = min(dp[cur][visited], dfs(i, visited | (1 << i)) + city[cur][i])

    if dp[cur][visited] == INF:
        dp[cur][visited] = -1
        return INF
    else:
        return dp[cur][visited]


print(dfs(0, 1))

