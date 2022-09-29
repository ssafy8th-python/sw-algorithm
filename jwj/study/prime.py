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

INF = int(1e9)


def prime():
    # U는 방문한 노드, D는 현재 노드엣 갈 수 있는 노드들의 가중치 값
    U = []
    D = [INF] * (V+1)
    D[0] = 0
    P = [INF] * (V+1)

    while len(U) < V+1:

        # 가장 작은 값 고르기
        minV = INF
        for i in range(V+1):
            if i in U: continue
            if minV > D[i]:
                minV = D[i]
                curV = i

        # 찾은 값을 방문 표시
        U.append(curV)

        # 위에서 찾은 값과 연결된 노드들의 값을 갱신해줌
        for i in range(V+1):
            if i in U:continue
            if G[curV][i] and D[i] > G[curV][i]:
                D[i] = G[curV][i]
                P[i] = curV

    print(U, D, P)


V, E = map(int, input().split())

G = [[0] * (V+1) for _ in range(V+1)]

for i in range(E):
    n1, n2, w = map(int, input().split())
    G[n1][n2] = w
    G[n2][n1] = w

prime()
