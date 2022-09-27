# 구간 합 구하기 4
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = list(map(int, input().split()))
for i in range(1, N):
    lst[i] += lst[i-1]

for _ in range(M):
    st, end = map(int, input().split())
    st, end = st-1, end-1
    if st == 0:
        print(lst[end])
    else:
        print(lst[end]-lst[st-1])

