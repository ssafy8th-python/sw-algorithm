# 1916 최소비용 구하기
# 주소: https://www.acmicpc.net/problem/1916

# 제출한 답1 시간초과
import sys
input = sys.stdin.readline


def dijk():
    u = []
    d = [1e10] * (N + 1)
    d[S] = 0
    while len(u) < (N + 1):
        minV = 1e10
        for i in range(N + 1):
            if i not in u and minV > d[i]:
                minV = d[i]
                curV = i
        if curV == D:
            return d[curV]

        u.append(curV)

        for i in range(N + 1):
            if i not in u and G[curV][i] > -1:
                d[i] = min(d[i], G[curV][i] + d[curV])


N = int(input())
M = int(input())

G = [[-1] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    F, T, C = map(int, input().split())
    if G[F][T] == -1:
        G[F][T] = C
    else:
        G[F][T] = min(G[F][T], C)

S, D = map(int, input().split())
print(dijk())
