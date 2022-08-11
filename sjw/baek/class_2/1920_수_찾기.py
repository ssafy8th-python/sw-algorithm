# 1920 수 찾기
# 주소: https://www.acmicpc.net/problem/1920

# 제출한 답
import sys
input = sys.stdin.readline

N = int(input())
N_lst = list(map(int, input().split()))
M = int(input())
M_lst = list(map(int, input().split()))

N_lst.sort()

for i in M_lst:
    start = 0
    end = N - 1
    while True:
        mid = (start + end) // 2
        if start > end:
            print(0)
            break
        elif i == N_lst[mid]:
            print(1)
            break
        elif i < N_lst[mid]:
            end = mid - 1
        elif i > N_lst[mid]:
            start = mid + 1
