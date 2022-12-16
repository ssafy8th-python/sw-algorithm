# 15666 N과 M(12)
# 주소: https://www.acmicpc.net/problem/15666

# 제출한 답
import sys
input = sys.stdin.readline


def per(s, k):
    if k == M:
        print(*result)
    else:
        for i in range(s, N):
            result.append(n_lst[i])
            per(i, k + 1)
            result.pop()


N, M = map(int, input().split())
n_lst = sorted(list(set(map(int, input().split()))))
N = len(n_lst)
result = []
per(0, 0)
