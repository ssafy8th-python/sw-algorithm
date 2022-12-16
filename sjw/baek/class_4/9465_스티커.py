# 9465 스티커
# 주소: https://www.acmicpc.net/problem/9465

# 제출한 답1  틀렸습니다.
# import sys
# input = sys.stdin.readline
#
# T = int(input())
# for _ in range(T):
#     n = int(input())
#     stickers = [list(map(int, input().split())) for _ in range(2)]
#     sumV = {0: stickers[0][0], 1:stickers[1][0]}
#     sumIdx = [0, 1]
#     idx = 0
#     while idx < n - 1:
#         if idx + 2 < n:
#             for i in range(2):
#                 if sumIdx[i] == 0:
#                     if stickers[1][idx + 1] + stickers[0][idx + 2] > stickers[1][idx + 2]:
#                         sumV[i] += stickers[1][idx + 1] + stickers[0][idx + 2]
#                     else:
#                         sumV[i] += stickers[1][idx + 2]
#                         sumIdx[i] = 1
#                 else:
#                     if stickers[0][idx + 1] + stickers[1][idx + 2] > stickers[0][idx + 2]:
#                         sumV[i] += stickers[0][idx + 1] + stickers[1][idx + 2]
#                     else:
#                         sumV[i] += stickers[0][idx + 2]
#                         sumIdx[i] = 0
#             idx += 2
#         else:
#             for i in range(2):
#                 if sumIdx[i] == 0:
#                     sumV[i] += stickers[1][idx + 1]
#                 else:
#                     sumV[i] += stickers[0][idx + 1]
#             idx += 1
#
#     print(max(sumV.values()))


# 제출한 답2
import sys
input = sys.stdin.readline

# DP: 하나의 숫자는 앞의 두 개를 더하거나 혹은 두 단계전의 숫자를 더한 경우 두 가지 중 하나

T = int(input())
for _ in range(T):
    n = int(input())
    stickers = [list(map(int, input().split())) for _ in range(2)]

    if n > 1:  # n이 1인 경우를 제외한 나머지의 경우
        # 처음 숫자 두 개는 미리 설정해 놓아야함
        stickers[0][1] += stickers[1][0]
        stickers[1][1] += stickers[0][0]

        # 두 가지 경우를 비교해서 더 큰 경우를 더함
        for i in range(2, n):
            for j in range(2):
                stickers[j][i] += max(stickers[(j + 1) % 2][i - 1], stickers[(j + 1) % 2][i - 2])

    print(max(stickers[0][n - 1], stickers[1][n - 1]))
