# 달란트
import sys
sys.stdin = open("input (5).txt", "r")
'''
10
10 3
20 5
30 9
40 12
50 12
60 23
70 23
80 32
90 32
100 32
'''

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    q, r = divmod(n, m)
    print(f'#{tc} {q**(m-r)*(q+1)**r}')
