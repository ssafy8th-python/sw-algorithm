# 18917 수열과 쿼리 38
# 주소: https://www.acmicpc.net/problem/18917

# 제출한 답
import sys
input = sys.stdin.readline

sumV = 0
xor = 0
for _ in range(int(input())):
    idx = list(map(int, input().split()))
    if idx[0] == 1:
        sumV += idx[1]
        xor ^= idx[1]
    elif idx[0] == 2:
        sumV -= idx[1]
        xor ^= idx[1]
    elif idx[0] == 3:
        print(sumV)
    elif idx[0] == 4:
        print(xor)
