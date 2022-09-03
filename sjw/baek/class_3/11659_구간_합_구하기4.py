# 11659 구간 합 구하기 4
# 주소: https://www.acmicpc.net/problem/11659

# 제출한 답
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

n_lst = list(map(int, input().split()))
for i in range(1, n):
    n_lst[i] = n_lst[i] + n_lst[i - 1]

for _ in range(m):
    i, j = map(int, input().split())

    if i == 1:
        print(n_lst[j - 1])
    else:
        print(n_lst[j - 1] - n_lst[i - 2])
