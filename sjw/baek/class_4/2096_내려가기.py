# 2096 내려가기
# 주소: https://www.acmicpc.net/problem/2096

# 제출한 답 (메모리 초과)
# import sys
# input = sys.stdin.readline
#
# N = int(input())
# lines = [list(map(int, input().split())) for _ in range(N)]
#
# max_lines = [[0] * 3 for _ in range(N)]
# min_lines = [[10] * 3 for _ in range(N)]
#
# for i in range(3):
#     max_lines[0][i], min_lines[0][i] = lines[0][i], lines[0][i]
#
# for r in range(N - 1):
#     for c in range(3):
#         for dr, dc in [(1, -1), (1, 0), (1, 1)]:
#             nr, nc = r + dr, c + dc
#             if 0 <= nc < 3:
#                 max_lines[nr][nc] = max(max_lines[nr][nc], max_lines[r][c] + lines[nr][nc])
#                 min_lines[nr][nc] = min(min_lines[nr][nc], min_lines[r][c] + lines[nr][nc])
#
# print(max(max_lines[N - 1]), min(min_lines[N - 1]))


# 제출한 답 2
import sys
input = sys.stdin.readline

N = int(input())

lines = list(map(int, input().split()))
max_lines = [[0] * 3 for _ in range(2)]
min_lines = [[1e10] * 3 for _ in range(2)]

for i in range(3):
    max_lines[0][i], min_lines[0][i] = lines[i], lines[i]

flag = True
read_r, write_r = 0, 1
for _ in range(N - 1):
    lines = list(map(int, input().split()))

    read_r = 0 if flag else 1
    write_r = 1 if flag else 0
    for c in range(3):
        for dc in range(-1, 2):
            nc = c + dc
            if 0 <= nc < 3:
                max_lines[write_r][nc] = max(max_lines[write_r][nc], max_lines[read_r][c] + lines[nc])
                min_lines[write_r][nc] = min(min_lines[write_r][nc], min_lines[read_r][c] + lines[nc])

    for i in range(3):
        max_lines[read_r][i] = 0
        min_lines[read_r][i] = 1e10
    flag = not flag

print_r = read_r if N == 1 else write_r
max_score, min_score = max(max_lines[print_r]), min(min_lines[print_r])

print(max_score, min_score)


# 댜른 답
# import sys
# input = sys.stdin.readline
#
# n = int(input())
# init = list(map(int, input().split()))
# maxDp = init
# minDp = init
# for _ in range(n - 1):
#     a, b, c = map(int, input().split())
#     maxDp = [a + max(maxDp[0], maxDp[1]), b + max(maxDp), c + max(maxDp[1], maxDp[2])]
#     minDp = [a + min(minDp[0], minDp[1]), b + min(minDp), c + min(minDp[1], minDp[2])]
#
# print(max(maxDp), min(minDp))
