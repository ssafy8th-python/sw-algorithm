# 1463 1로 만들기
# 주소: https://www.acmicpc.net/problem/1463

# 제출한 답
# import sys
# input = sys.stdin.readline

# n = int(input())
#
# result = [0, 0, 1, 1]
#
# for i in range(4, n + 1):
#     result.append(result[i - 1] + 1)
#     if i % 2 == 0:
#         result[i] = min(result[i], result[i // 2] + 1)
#     if i % 3 == 0:
#         result[i] = min(result[i], result[i // 3] + 1)
#
# print(result[n])


# 재귀로 풀이(메모이제이션 필수)
# def mkone(k):
#     if k == 2:
#         return 1
#     elif k == 3:
#         return 1
#     if k % 2 == 0:
#         result[k // 2] + 1
#     if k % 3 == 0:
#         result.append(mkone(k // 3) + 1)
#     result.append(mkone(k - 1) + 1)
#
#     return min(result)
#
#
# n = int(input())
# result = [0, 0, 1, 1]
# print(mkone(n))