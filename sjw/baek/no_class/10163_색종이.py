# 10163 색종이
# 주소: https://www.acmicpc.net/problem/10163

# 제출한 답
# import sys
# input = sys.stdin.readline
#
# board = [[0] * 1001 for _ in range(1001)]
#
# n = int(input())
#
# for i in range(1, n + 1):
#     rcwh = list(map(int, input().split()))
#
#     for r in range(rcwh[1], rcwh[1] + rcwh[3]):
#         for c in range(rcwh[0], rcwh[0] + rcwh[2]):
#             board[r][c] = i
#
# for i in range(1, n + 1):
#     result = 0
#
#     for r in range(1001):
#         for c in range(1001):
#             if board[r][c] == i:
#                 result += 1
#
#     print(result)


# 다른 답
import sys
input = sys.stdin.readline


n = int(input())
board = [[n + 1] * 1001 for _ in range(1001)]
result = [0] * n

for i in range(n):
    rcwh = list(map(int, input().split()))

    for r in range(rcwh[1], rcwh[1] + rcwh[3]):
        for c in range(rcwh[0], rcwh[0] + rcwh[2]):
            if board[r][c] != n + 1:
                result[board[r][c]] -= 1
                board[r][c] = i
                result[i] += 1
            else:
                board[r][c] = i
                result[i] += 1

for i in range(n):
    print(result[i])
