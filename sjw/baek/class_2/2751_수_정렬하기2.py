# 2751 수 정렬하기 2
# 주소: https://www.acmicpc.net/problem/2751

# 제출한 답
import sys
input = sys.stdin.readline

N = int(input())

num_lst = []

for _ in range(N):
    n = int(input())
    num_lst.append(n)

num_lst.sort()

for i in num_lst:
    print(i)
