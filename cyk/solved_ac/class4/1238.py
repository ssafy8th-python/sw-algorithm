# 파티
INF = 10e5
def dijk(arr):
    U = [False]*(N+1)
    D = [INF]*(N+1)
    D[X] = 0

    while U.count(True) < N:
        minV = INF
        for i in range(N+1):
            if U[i]: continue
            if minV > D[i]:
                minV = D[i]
                curV = i
        U[curV] = True
        for i in range(N+1):
            if U[i]: continue
            D[i] = min(D[i], D[curV]+arr[curV][i])
    return D
N, M, X = map(int, input().split())
G1 = [[INF]*(N+1) for _ in range(N+1)]
G2 = [[INF]*(N+1) for _ in range(N+1)]

for _ in range(M):
    s, e, w = map(int, input().split())
    G1[s][e] = w
    G2[e][s] = w

go = dijk(G1)
come = dijk(G2)
res = 0
for i in range(1, N+1):
    tmp = go[i]+come[i]
    if res < tmp:
        res = tmp
print(res)