# 해킹
import sys, heapq
input = sys.stdin.readline
INF = 10e5

def dijk():
    U = [False]*(N+1)
    q = [(0, C)]
    D = []
    while q:
        cost, curV = heapq.heappop(q)

        if U[curV]: continue

        U[curV] = True
        D.append(cost)

        for curCost, curNode in COM[curV]:
            heapq.heappush(q, (curCost+cost, curNode))

    print(len(D), D[-1])


T = int(input())
for _ in range(T):
    N, d, C = map(int, input().split()) # 컴퓨터 개수, 의존성 개수, 해킹당한 컴퓨터 번호
    COM = [[] for _ in range(N+1)]
    for _ in range(d):
        s, e, w = map(int, input().split())
        COM[e].append((w, s))
    dijk()


 #
    # while U.count(True) < N:
    #     minV = INF
    #     for i in range(N+1):
    #         if U[i]:continue
    #         if minV > D[i]:
    #             minV = D[i]
    #             curV = i
    #     if minV == INF:
    #         break
    #
    #     U[curV] = True
    #     for i in range(N+1):
    #         if U[i]:continue
    #         if D[i] >= COM[curV][i]:
    #             D[i] = D[curV]+COM[curV][i]
    # print(U.count(True), end=' ')
    # for i in range(N, -1, -1):
    #     if U[i] == True:
    #         print(D[i])
    #         break
    #
    # return

