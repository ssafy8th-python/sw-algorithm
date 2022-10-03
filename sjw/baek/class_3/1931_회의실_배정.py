# 1931 회의실 배정
# 주소: https://www.acmicpc.net/problem/1931

# 제출한 답
import sys
input = sys.stdin.readline

N = int(input())
N_lst = [list(map(int, input().split())) for _ in range(N)]
N_lst.sort(key=lambda x: (x[1], x[0]))

cnt, i = 1, 1
ne = N_lst[0][1]
while i < N:
    if N_lst[i][0] >= ne:
        ne = N_lst[i][1]
        cnt += 1
    i += 1

print(cnt)
