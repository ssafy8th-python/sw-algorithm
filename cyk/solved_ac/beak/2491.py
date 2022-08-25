# 수열
# 수열 안에서 연속해서 커지거나 연속해서 작아지는 수열 중 가장 길이가 긴 것을 찾아내어 그 길이 출력
import sys
input = sys.stdin.readline
up = 0      # 같거나 커질때
down = 0    # 같거나 작아질때
mx = 0
n = int(input())
s = list(map(int, input().split()))
for i in range(n-1):
    if s[i] <= s[i+1]:
        up += 1
    else:
        if mx < up:
            mx = up
        up = 0
    if s[i] >= s[i+1]:
        down += 1
    else:
        if mx < down:
            mx = down
        down = 0
if mx < up:
    mx = up
if mx < down:
    mx = down
print(mx+1)