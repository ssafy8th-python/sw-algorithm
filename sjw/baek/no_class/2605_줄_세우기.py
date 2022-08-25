# 2605 줄 세우기
# 주소: https://www.acmicpc.net/problem/2605

# 제출한 답
import sys
input = sys.stdin.readline

n = int(input())
order = list(map(int, input().split()))
lst = [0]
for i in range(n):
    lst.insert(i + 1 - order[i], i + 1)

print(*lst[1:])
