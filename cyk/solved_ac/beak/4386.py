# 별자리 만들기
def prim():
    INF = 1000
    U = []
    D = [INF] * N
    D[0] = 0
    while len(U) < N:
        minV = INF
        for i in range(N):
            if i in U: continue
            if minV > D[i]:
                minV = D[i]
                curV = i
        U.append(curV)

        for i in range(N):
            if i in U: continue
            if G[curV][i] and D[i] > G[curV][i]:
                D[i] = G[curV][i]
    print(round(sum(D), 2))


N = int(input())
ipt = [list(map(float, input().split())) for _ in range(N)]

G = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if i != j:
            G[i][j] = ((ipt[i][0] - ipt[j][0]) ** 2 + (ipt[i][1] - ipt[j][1]) ** 2) ** 0.5

prim()