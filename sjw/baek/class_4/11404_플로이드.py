# 11404 플로이드
# 주소: https://www.acmicpc.net/problem/11404

# 제출한 답1
# import sys
# input = sys.stdin.readline
#
# n = int(input())
# m = int(input())
#
# nodes = [[1e10] * n for _ in range(n)]
# for _ in range(m):
#     a, b, c = map(int, input().split())
#     nodes[a - 1][b - 1] = min(nodes[a - 1][b - 1], c)
#
# for i in range(n):
#     nodes[i][i] = 0
#
# for k in range(n):
#     for s in range(n):
#         for e in range(n):
#             nodes[s][e] = min(nodes[s][k] + nodes[k][e], nodes[s][e])
#
# for i in range(n):
#     for j in range(n):
#         if nodes[i][j] == 1e10:
#             nodes[i][j] = 0
#
# for i in range(n):
#     print(*nodes[i])


# 제출한 답2
# import sys
# input = sys.stdin.readline
#
# n = int(input())
# m = int(input())
# INF = 1e10
# nodes = [[INF] * n for _ in range(n)]
# for i in range(n):
#     nodes[i][i] = 0
#
# for _ in range(m):
#     a, b, c = map(int, input().split())
#     nodes[a - 1][b - 1] = min(nodes[a - 1][b - 1], c)
#
#
# for k in range(n):
#     for s in range(n):
#         for e in range(n):
#             nodes[s][e] = min(nodes[s][k] + nodes[k][e], nodes[s][e])
#
# for i in range(n):
#     print(*[0 if x == INF else x for x in nodes[i]])


# 제출한 답3
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
INF = 1e10
nodes = [[INF] * n for _ in range(n)]
for i in range(n):
    nodes[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    if nodes[a - 1][b - 1] > c:
        nodes[a - 1][b - 1] = c


for k in range(n):
    for s in range(n):
        for e in range(n):
            if nodes[s][e] > nodes[s][k] + nodes[k][e]:
                nodes[s][e] = nodes[s][k] + nodes[k][e]

for i in range(n):
    print(*[0 if x == INF else x for x in nodes[i]])


# 다른 답
import sys
input = sys.stdin.readline


def solution():
    n = int(input())
    m = int(input())

    INF = 1000000000
    distance = [[INF] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        distance[i][i] = 0

    for _ in range(m):
        a, b, c = map(int, input().split())
        if distance[a][b] > c:
            distance[a][b] = c

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if distance[i][j] > distance[i][k] + distance[k][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]

    for i in range(1, n + 1):
        print(*[x if x != INF else 0 for x in distance[i][1:]])


solution()
