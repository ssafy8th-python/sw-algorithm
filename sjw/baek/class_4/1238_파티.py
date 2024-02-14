# 1238 파티
# 주소: https://www.acmicpc.net/problem/1238

# 제출한 답 64ms
import sys
input = sys.stdin.readline
import heapq


def dijkstra(g, n, x):
    distance = [1e10] * (n + 1)
    distance[x] = 0

    heap = []
    heapq.heappush(heap, [0, x])

    visited = [0] * (n + 1)
    while heap:
        w, u = heapq.heappop(heap)
        visited[u] = 1
        for v, t in g[u]:
            if not visited[v]:
                newW = w + t
                if distance[v] > newW:
                    distance[v] = newW
                    heapq.heappush(heap, [newW, v])

    return distance


N, M, X = map(int, input().split())

go = [[] for _ in range(N + 1)]
back = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B, T = map(int, input().split())
    go[A].append([B, T])
    back[B].append([A, T])

goTime = dijkstra(go, N, X)
backTime = dijkstra(back, N, X)

answer = 0
for i in range(1, N + 1):
    times = goTime[i] + backTime[i]
    if times > answer:
        answer = times

print(answer)


# 제출한 답2 76ms
import sys
from collections import deque

input = sys.stdin.readline


def dijkstra(g, n, x):
    distance = [1e10] * (n + 1)
    distance[x] = 0

    q = deque([x])

    while q:
        u = q.popleft()
        for v, t in g[u]:
            if distance[v] > (newW := distance[u] + t):
                distance[v] = newW
                q.append(v)

    return distance


N, M, X = map(int, input().split())

go = [[] for _ in range(N + 1)]
back = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B, T = map(int, input().split())
    go[A].append([B, T])
    back[B].append([A, T])

goTime = dijkstra(go, N, X)
backTime = dijkstra(back, N, X)

answer = 0
for i in range(1, N + 1):
    times = goTime[i] + backTime[i]
    if times > answer:
        answer = times

print(answer)


# 다른 답 56ms
# import sys
# import math
#
#
# def make_adj_arr(num_of_node, num_of_edge):
#     adj_list = [[] for i in range(num_of_node + 1)]
#     adv_adj_list = [[] for i in range(num_of_node + 1)]
#
#     for i in range(num_of_edge):
#         st, fin, time = map(int, sys.stdin.readline().split())
#
#         adj_list[st].append([fin, time])
#         adv_adj_list[fin].append([st, time])
#
#     return adj_list, adv_adj_list
#
#
# def mintime(adj_list, start_node, num_of_node):
#     min_time_list = [math.inf for i in range(num_of_node + 1)]
#
#     queue = [start_node]
#     min_time_list[start_node] = 0
#
#     while queue:
#         curr_node = queue.pop(0)
#
#         for adj_node in adj_list[curr_node]:
#             if (temp := min_time_list[curr_node] + adj_node[1]) < min_time_list[adj_node[0]]:
#                 min_time_list[adj_node[0]] = temp
#                 queue.append(adj_node[0])
#
#     return min_time_list
#
#
# N, M, X = map(int, sys.stdin.readline().split())
# back_to_home, go_party = make_adj_arr(N, M)
#
# time1 = mintime(go_party, X, N)
# time2 = mintime(back_to_home, X, N)
# time_sum = []
# for i in range(1, N + 1):
#     time_sum.append(time1[i] + time2[i])
#
# print(max(time_sum))
#
#
