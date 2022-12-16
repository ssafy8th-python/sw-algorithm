# 11053 가장 긴 증가하는 부분 수열
# 주소: https://www.acmicpc.net/problem/11053

# 제출한 답
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

check = [0] * N
check[0] = 1
for i in range(1, N):
    cnt = 0
    for j in range(i):
        if arr[j] < arr[i]:
            cnt = max(cnt, check[j])
    check[i] = cnt + 1

print(max(check))