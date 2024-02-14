# 1167 트리의 지름
# 주소: https://www.acmicpc.net/problem/1167

# 제출한 답1 1372ms
# import sys
# input = sys.stdin.readline
#
#
# def dfs(start):
#     visited = [0] * (V + 1)
#     stack = [[start, 0]]
#     visited[start] = 1
#
#     node, distance = start, 0
#     while stack:
#         cNode, cDistance = stack.pop()
#         if cDistance > distance:
#             distance = cDistance
#             node = cNode
#
#         if parents[cNode]:
#             p, w = parents[cNode]
#             if not visited[p]:
#                 visited[p] = 1
#                 stack.append([p, cDistance + w])
#         for c, w in children[cNode]:
#             if not visited[c]:
#                 visited[c] = 1
#                 stack.append([c, cDistance + w])
#
#     return [node, distance]
#
#
# V = int(input())
# parents = [0] * (V + 1)
# children = [[]for _ in range(V + 1)]
#
# for _ in range(1, V + 1):
#     node = list(map(int, input().split()))
#     p = node[0]
#     for i in range(1, len(node) - 1, 2):
#         c, w = node[i], node[i + 1]
#         children[p].append([c, w])
#         parents[c] = [p, w]
#
# node1, tmp = dfs(1)
# node2, answer = dfs(node1)
#
# print(answer)


# 제출한 답2 780ms
import sys
input = sys.stdin.readline


def dfs(start):
    visited = [0] * (V + 1)
    stack = [[start, 0]]
    visited[start] = 1

    node, distance = start, 0
    while stack:
        cNode, cDistance = stack.pop()
        if cDistance > distance:
            distance = cDistance
            node = cNode

        for c, w in children[cNode]:
            if not visited[c]:
                visited[c] = 1
                stack.append([c, cDistance + w])

    return [node, distance]


V = int(input())
children = [[]for _ in range(V + 1)]

for _ in range(1, V + 1):
    node = list(map(int, input().split()))
    p = node[0]
    for i in range(1, len(node) - 1, 2):
        c, w = node[i], node[i + 1]
        children[p].append([c, w])

node1, tmp = dfs(1)
node2, answer = dfs(node1)

print(answer)


# 다른 답
# import sys
#
# input = sys.stdin.readline
#
# n = int(input())
# tree = [[] for _ in range(n + 1)]
#
# for _ in range(n):
#     seq = list(map(int, input().split()))
#     node = seq[0]
#     index = 1
#     while seq[index] != -1:
#         adj_node, adj_cost = seq[index], seq[index + 1]
#         tree[node].append((adj_node, adj_cost))
#         index = index + 2
#
# visit = [-1] * (n + 1)
# visit[1] = 0
#
#
# def dfs(node, dist):
#     for v, d in tree[node]:
#         cal_dist = dist + d
#         if visit[v] == -1:
#             visit[v] = cal_dist
#             dfs(v, cal_dist)
#
#     return
#
#
# dfs(1, 0)
# temp = [0, 0]
# for i in range(1, len(visit)):
#     if visit[i] > temp[1]:
#         temp[1] = visit[i]
#         temp[0] = i
#
# visit = [-1] * (n + 1)
# visit[temp[0]] = 0
# dfs(temp[0], 0)
# print(max(visit))