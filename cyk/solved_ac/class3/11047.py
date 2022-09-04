# 동전 0
'''
10 4200
1
5
10
50
100
500
1000
5000
10000
50000
'''
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
s = sorted([int(input()) for _ in range(N)], reverse=True)
cnt = 0
for elem in s:
    while K - elem >= 0:
        K -= elem
        cnt += 1
    if K == 0:
        print(cnt)
        break