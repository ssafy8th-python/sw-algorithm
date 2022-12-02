# 23083 꿀벌 승연이
# 주소: https://www.acmicpc.net/problem/23083

# 제출한 답 1 => 틀림(시간초과)

# (0, 0)에서 (N - 1, M - 1) 까지 가는 모든 경로의 수
# 완탐을 하는 것이므로 BFS, DFS 모두 가능
# 홀수 일때와 짝수일때 갈 수 있는 방향이 다름
# 문제와 다르게 짝수, 홀수를 반대로 봐야함
# 아래 오른위 오른아래만 이동 가능
# 짝수일 때: (1, 0), (0, 1), (-1, 1)
# 홀수일 때: (1, 0), (0, 1), (1, 1)

# import sys
# input = sys.stdin.readline
#
# delta = {                          # 홀수와 짝수일 때 이동가능 방향
#     0: [(1, 0), (0, 1), (-1, 1)],
#     1: [(1, 0), (0, 1), (1, 1)]
# }
#
#
# def DFS(S):
#     stack = [S]
#     while stack:
#         r, c = stack.pop()
#         hive[r][c] += 1  # 몇 번째 방문했는지 기록
#         for dr, dc in delta.get(c % 2):
#             nr, nc = r + dr, c + dc
#             if 0 <= nr < N and 0 <= nc < M and hive[nr][nc] != -1:  # 범위를 안 벗어나고 구멍이 아니라면
#                 stack.append((nr, nc))  # 스택
#
#
# N, M = map(int, input().split())     # 문제에서 (1, 1) ~ (N, M) 까지 있으므로,
# K = int(input())                     # (0, 0) == (1, 1)로 생각하여 풀이
# hive = [[0] * M for _ in range(N)]
# for _ in range(K):
#     x, y = map(int, input().split())
#     hive[x - 1][y - 1] = -1  # 입력값과 배열사이의 차이를 없애기 위한 x - 1, y - 1
# DFS((0, 0))
# print(hive[N - 1][M - 1] % int((1e9 + 7)))


# 제출한 답 2  2408ms
# 각 칸으로 갈 수 있는 모든 횟수 적어나감
# 최대 1000 * 1000 * 3 번 반복
# 좌상부터 열우선 순회로 계산
# 0열은 전부 1임
# 짝수일 때: (-1, 0), (0, -1), (-1, -1)
# 홀수일 때: (-1, 0), (0, -1), (1, -1)
import sys
input = sys.stdin.readline

N, M = map(int, input().split())     # 문제에서 (1, 1) ~ (N, M) 까지 있으므로,
hive = [[0] * M for _ in range(N)]   # (0, 0) == (1, 1)로 생각하여 풀이
for _ in range(int(input())):
    x, y = map(int, input().split())
    hive[x - 1][y - 1] = -1  # 입력값과 배열사이의 차이를 없애기 위한 x - 1, y - 1
hive[0][0] = 1
delta = {                            # 홀수와 짝수일 때 값을
    0: [(-1, 0), (0, -1), (-1, -1)],
    1: [(-1, 0), (0, -1), (1, -1)]
}
for c in range(M):
    for r in range(N):
        if hive[r][c] >= 0:
            for dr, dc in delta.get(c % 2):
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < M and hive[nr][nc] >= 0:
                    hive[r][c] += hive[nr][nc]

print(hive[N - 1][M - 1] % int((1e9 + 7)))


# 다른 답  876ms
import sys

# 입력값
N, M = map(int, input().split())
dp = [[0] * M for _ in range(N)]   # (N + 1) 왜하지? => 범위를 벗어나는지 확인안하고 무조건 더하기 위함
dp[0][0] = 1
hole = {(0, 0)}     # set으로 만듦
mod = 10 ** 9 + 7

# 빈구멍 입력받아서 set에 넣었다치고
# for line in sys.stdin:   # ??? 작동안함
#     i, j = map(int, line.split())
for _ in range(int(input())):
    x, y = map(int, input().split())
    hole.add((x - 1, y - 1))


for j in range(M):
    for i in range(N):
        if (i, j) in hole:  # 구멍이면 스킵
            continue
        elif j % 2:     # 홀수면
            dp[i][j] = (dp[i + 1][j - 1] + dp[i][j - 1] + dp[i - 1][j]) % mod
        else:
            dp[i][j] = (dp[i][j - 1] + dp[i - 1][j - 1] + dp[i - 1][j]) % mod

print(dp[-2][-1])