# 9251 LCS
# 주소: https://www.acmicpc.net/problem/9251

# 제출한 답1
# import sys
# input = sys.stdin.readline
#
# first = input().strip()
# second = input().strip()
# dp = [[0] * (len(second) + 1) for _ in range(len(first) + 1)]
#
# for i in range(len(first)):
#     for j in range(len(second)):
#         if first[i] == second[j]:
#             dp[i + 1][j + 1] = dp[i][j] + 1
#         else:
#             dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
#
# print(dp[len(first)][len(second)])


# 다른 답
import sys
read = sys.stdin.readline

word1, word2 = read().strip(), read().strip()
l1, l2 = len(word1), len(word2)
cache = [0] * l2

for i in range(l1):
    cnt = 0
    for j in range(l2):
        if cnt < cache[j]:
            cnt = cache[j]
        elif word1[i] == word2[j]:
            cache[j] = cnt + 1
print(max(cache))
