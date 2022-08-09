# 1920 수 찾기
# 주소: https://www.acmicpc.net/problem/1920

# 제출한 답 5 2 3
#          4 2 2
import sys
input = sys.stdin.readline

N = int(input())
N_lst = list(map(int, input().split()))
M = int(input())
M_lst = list(map(int, input().split()))

N_lst.sort()

for i in M_lst:
    start = 0
    end = N

    while True:
        if i == N_lst[(end - start)//2]:
            print(1)
            break
        elif start > end:
            print(0)
            break
        elif i < N_lst[(end - start)//2] and end >= start:
            end = (end - start)//2 - 1
        elif i > N_lst[(end - start)//2] and end >= start:
            start = (end - start)//2 + 1
