# 최소 이동 거리
# 0번 지점에서 N번 지점까지 이동하는데 걸리는 최소한의 거리
import sys
sys.stdin = open("sample_input (4).txt", "r")

def dijk():
    U = []
    D = [100] * (V+1)
    D[0] = 0

    while len(U) < V+1:
        minV = 100
        for i in range(V+1):
            if i in U: continue
            if minV > D[i]:
                minV = D[i]
                curV = i

        U.append(curV)
        for i in range(V+1):
            if i in U: continue
            if G[curV][i] and D[i] > D[curV] + G[curV][i]:
                D[i] = D[curV] + G[curV][i]
    print(f'#{tc} {D[-1]}')

T = int(input())
for tc in range(1, 1+T):
    V, E = map(int, input().split())
    G = [[0]*(V+1) for _ in range(V+1)]

    for _ in range(E):
        n1, n2, w = map(int, input().split())
        G[n1][n2] = w

    dijk()