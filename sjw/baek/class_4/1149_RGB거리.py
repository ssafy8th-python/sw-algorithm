# 1149 RGB거리
# 주소: https://www.acmicpc.net/problem/1149

# 제출한 답1  시간 초과 or RecursionError
# import sys
# input = sys.stdin.readline


# def minCost(k, curC, lastC, ideal):
#     global result
#     if curC >= result or (curC + ideal) >= result:
#         return
#     elif k == N:
#         result = min(curC, result)
#     else:
#         minC = min(costs[k])
#         tmp = 10000
#         j = -1
#         for i in range(3):
#             if lastC != i:
#                 if tmp > costs[k][i]:
#                     tmp = costs[k][i]
#                     j = i
#         minCost(k + 1, curC + tmp, j, ideal - minC)
#
#
# N = int(input())
# costs = [list(map(int, input().split())) for _ in range(N)]
# result = 10000000
# idealC = 0
# for cost in costs:
#     idealC += min(cost)
#
# minCost(0, 0, -1, idealC)
# print(result)


# 제출한 답2  시간 초과
# import sys
# input = sys.stdin.readline
#
#
# def dfs():
#     global result
#     s = [(0, 0, -1, idealC)]
#
#     while s:
#         v = s.pop()
#         if v[1] >= result or (v[1] + v[3]) >= result:
#             continue
#         elif v[0] == N:
#             result = min(v[1], result)
#         else:
#             minC = min(costs[v[0]])
#             for i in range(3):
#                 if v[2] != i:
#                     s.append((v[0] + 1, v[1] + costs[v[0]][i], i, v[3] - minC))
#
#
# N = int(input())
# costs = [list(map(int, input().split())) for _ in range(N)]
# result = 10000000
# idealC = 0
# for cost in costs:
#     idealC += min(cost)
# dfs()
# print(result)


# 제출한 답3  40ms
import sys
input = sys.stdin.readline

N = int(input())
costs = [list(map(int, input().split())) for _ in range(N)]

for i in range(1, N):
    for j in range(3):
        costs[i][j] += min(costs[i - 1][j - 1], costs[i - 1][j - 2])

print(min(costs[-1]))


# 다른 답  36ms
import sys

N = int(sys.stdin.readline())
B = []
DP = [[0] * 3 for i in range(N)]
for i in range(N):
    B.append(list(map(int, sys.stdin.readline().split())))

DP[0][0] = B[0][0]
DP[0][1] = B[0][1]
DP[0][2] = B[0][2]
for i in range(1, N):
    DP[i][0] = min(B[i][0]+DP[i-1][1], B[i][0]+DP[i-1][2])
    DP[i][1] = min(B[i][1]+DP[i-1][0], B[i][1]+DP[i-1][2])
    DP[i][2] = min(B[i][2]+DP[i-1][0], B[i][2]+DP[i-1][1])

print(min(DP[-1]))
