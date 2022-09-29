'''
6 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
'''


def prim():
    U = []
    D = [10000] * (N+1)
    D[0] = 0
    P = [10000] * (N+1)
    while len(U) < (N+1):
        # U에 D 중 가장 작은 값을 가진 정점을 선택

        # U에 가장 작은 값은 넣어줌
        minV = 100000
        for i in range(N + 1):
            if i in U: continue  # U안에 있으면 갈필요 없음
            if minV > D[i]:
                minV = D[i]
                curV = i

        U.append(curV)

        # 해당 값과 연결된 정점들의 D값을 최선으로 바꿔줍니다.
        for i in range(N+1):
            if i in U: continue
            if G[curV][i] and D[i] > G[curV][i]:
                D[i] = G[curV][i]
                P[i] = curV

    print(U, D, P)


N, E = map(int, input().split())
G = [[0] * (N + 1) for _ in range(N+1)]

for i in range(E):
    n1, n2, w = map(int, input().split())
    G[n1][n2] = w
    G[n2][n1] = w

prim()