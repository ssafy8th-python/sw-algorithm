# 1697 숨바꼭질
# 주소: https://www.acmicpc.net/problem/1697

# 제출한 답
import sys
input = sys.stdin.readline


def superSubin(t):
    global time


n, k = map(int, input().split())
time = 0
while n <= k:
    n *= 2
    time += 1
print(time)
time1 = time + (n - k)
time2 = time + (k - n // 2) - 1
print(min(time1, time2))
