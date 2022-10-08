# 15650 N과 M(2)
# 주소: https://www.acmicpc.net/problem/15650

# 제출한 답
# import sys
# input = sys.stdin.readline
#
#
# def per(d, n, r):
#     if d == r:
#         tmp = sorted(p)
#         if tmp not in result:
#             result.append(tmp)
#             print(*tmp)
#     else:
#         for i in range(n):
#             if not check[i]:
#                 check[i] = 1
#                 p[d] = lst[i]
#                 per(d + 1, n, r)
#                 check[i] = 0
#
#
# N, M = map(int, input().split())
#
# result = []
# lst = [i for i in range(1, N + 1)]
# check = [0] * N
# p = [0] * M
# per(0, N, M)


# 다른 답

def com(d, s):
    if d == M:
        print(*c)
    else:
        for i in range(s, N):
            c[d] = lst[i]
            com(d + 1, i + 1)


N, M = map(int, input().split())
lst = [i for i in range(1, N + 1)]
c = [0] * M
com(0, 0)
