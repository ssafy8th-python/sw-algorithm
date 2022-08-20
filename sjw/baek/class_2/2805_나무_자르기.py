# 2805 나무 자르기
# 주소: https://www.acmicpc.net/problem/2805

# 제출한 답
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().split()))

low = 1
high = 1000000000

while low <= high:
    mid = (low + high) // 2

    cnt = 0
    for i in trees:
        if i > mid:
            cnt += i - mid
            if cnt >= m:
                break

    if cnt >= m:
        low = mid + 1
    else:
        high = mid - 1

print(high)
