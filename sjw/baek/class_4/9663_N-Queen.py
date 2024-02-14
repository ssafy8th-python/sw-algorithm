# 9663 N-Queen
# 주소: https://www.acmicpc.net/problem/9663

# 제출한 답 (PyPy3 15928ms)
# import sys
# input = sys.stdin.readline
#
#
# def queen(row, N):
#     global answer
#     if row == N:
#         answer += 1
#     else:
#         for nCol in range(N):
#             flag = True
#             for i in range(row):
#                 if board[i] == nCol:
#                     flag = False
#                 elif row - i == abs(nCol - board[i]):
#                     flag = False
#                 if not flag:
#                     break
#             if flag:
#                 board[row] = nCol
#                 queen(row + 1, N)
#
#
# N = int(input())
# board = [0] * N
# answer = 0
# queen(0, N)
#
# print(answer)


# 다른 답1 (PyPy3 4560ms)
# n = int(input())
#
# flag_1 = [0] * n
# flag_2 = [0] * (2 * n - 1)
# flag_3 = [0] * (2 * n - 1)
#
# cnt = 0
#
#
# def nQueen(depth):
#     global cnt
#     if depth == n:
#         cnt += 1
#         return
#
#     for i in range(n):
#         if not(flag_1[i] or flag_2[i + depth] or flag_3[n + depth - i - 1]):
#             flag_1[i], flag_2[i + depth], flag_3[n + depth - i - 1] = 1, 1, 1
#             nQueen(depth + 1)
#             flag_1[i], flag_2[i + depth], flag_3[n + depth - i - 1] = 0, 0, 0
#
#
# nQueen(0)
# print(cnt)


# # 다른 답2 (PyPy3 4896ms)
def dfs(n):
    global ans
    if n == N:
        ans += 1
        return

    for j in range(N):  # 열번호
        if v1[j] == 0 and v2[n + j] == 0 and v3[n - j] == 0:
            v1[j], v2[n + j], v3[n - j] = 1, 1, 1
            dfs(n + 1)
            v1[j], v2[n + j], v3[n - j] = 0, 0, 0


N = int(input())
ans = 0
v1, v2, v3 = [[0] * (2 * N) for _ in range(3)]
dfs(0)
print(ans)


# 다른 답3 (Python3 9776ms)
# def solve(row, ld, rd):
#     if row == ALL_ONES:
#         return 1
#
#     count = 0
#     pos = ALL_ONES & ~(row | ld | rd)
#     while pos:
#         p = pos & -pos  # 가장 오른쪽 1비트를 가져옴
#         pos -= p  # p 위치의 비트를 끔
#         count += solve(row+p, (ld+p) << 1, (rd+p) >> 1)
#     return count
#
#
# N = int(input())
# ALL_ONES = (1 << N) - 1  # N개의 모든 비트가 1인 수
#
# print(solve(0, 0, 0))
#
#
