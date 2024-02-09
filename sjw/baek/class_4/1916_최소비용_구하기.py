# 1916 최소비용 구하기
# 주소: https://www.acmicpc.net/problem/1916

# 제출한 답1 시간초과
# import sys
# input = sys.stdin.readline
#
#
# def dijk():
#     u = []
#     d = [1e10] * (N + 1)
#     d[S] = 0
#     while len(u) < (N + 1):
#         minV = 1e10
#         for i in range(N + 1):
#             if i not in u and minV > d[i]:
#                 minV = d[i]
#                 curV = i
#         if curV == D:
#             return d[curV]
#
#         u.append(curV)
#
#         for i in range(N + 1):
#             if i not in u and G[curV][i] > -1:
#                 d[i] = min(d[i], G[curV][i] + d[curV])
#
#
# N = int(input())
# M = int(input())
#
# G = [[-1] * (N + 1) for _ in range(N + 1)]
# for _ in range(M):
#     F, T, C = map(int, input().split())
#     if G[F][T] == -1:
#         G[F][T] = C
#     else:
#         G[F][T] = min(G[F][T], C)
#
# S, D = map(int, input().split())
# print(dijk())


# 제출한 답2
import sys
from heapq import heappop, heappush


def dijk(graph, start):
    total_costs = [1e10] * (N + 1)
    total_costs[start] = 0
    queue = []
    heappush(queue, (start, total_costs[start]))
    while queue:
        node, cost = heappop(queue)

        if total_costs[node] < cost:
            continue

        for next_node, next_cost in graph[node]:
            new_cost = total_costs[node] + next_cost
            if new_cost < total_costs[next_node]:
                total_costs[next_node] = new_cost
                heappush(queue, (next_node, new_cost))

    return total_costs


input = sys.stdin.readline
N = int(input())
M = int(input())

GRAPH = [[] for _ in range(N + 1)]
for _ in range(M):
    DEPART, ARRIVE, COST = map(int, input().split())
    GRAPH[DEPART].append([ARRIVE, COST])
START, END = map(int, input().split())

print(dijk(GRAPH, START)[END])
