# 로프
# 1 <= N <= 1000000 개의 로프
'''
3
1
5
9
'''
import sys
input = sys.stdin.readline
N = int(input())
rope = sorted([int(input()) for _ in range(N)])
maxV = 0
for idx, elem in enumerate(rope):
    if maxV < (N-idx) * elem:
        maxV = (N-idx) * elem
print(maxV)