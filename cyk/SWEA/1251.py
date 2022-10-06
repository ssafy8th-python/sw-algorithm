# 하나로
# 모든 섬을 연결해야하는 프로젝트
# 환경부담금 : E x L ^2
# 환경부담금을 최소로 지불하여 N개의 모든 섬을 연결할 수 있는 교통 시스템 설계
import sys
# sys.stdin = open("re_sample_input.txt","r")

def prim():
    U = []
    D = [MAX] * (N)
    D[0] = 0
    while len(U) < N:
        minV = MAX
        for i in range(N):
            if i in U:continue
            if minV > D[i]:
                minV = D[i]
                curV = i

        U.append(curV)

        for i in range(N):
            if i in U:continue
            if G[curV][i] and D[i] > G[curV][i]:
                D[i] = G[curV][i]

    print(f'#{tc} {round(sum(D))}')

T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    x_Lst = list(map(int, input().split()))
    y_Lst = list(map(int, input().split()))
    E = float(input())

    G = [[0]*N for _ in range(N)]

    MAX = 0
    for i in range(N):
        for j in range(N):
            if i != j:
                w = ((x_Lst[i] - x_Lst[j]) **2 + (y_Lst[i] - y_Lst[j]) **2) * E
                G[i][j] = w
                MAX += w
    MAX += 1

    prim()

