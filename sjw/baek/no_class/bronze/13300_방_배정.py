# 13300 방 배정
# 주소: https://www.acmicpc.net/problem/13300

# 제출한 답
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

grades = [[0, 0] for _ in range(7)]

for _ in range(n):
    s, y = map(int, input().split())
    grades[y][s] += 1

cnt = 0
for year in grades:
    for i in year:
        if i % k:
            cnt += i // k + 1
        else:
            cnt += i // k

print(cnt)
