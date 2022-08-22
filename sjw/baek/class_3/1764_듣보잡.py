# 1764 듣보잡
# 주소: https://www.acmicpc.net/problem/1764

# 제출한 답
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
set_n = set()
set_m = set()

for _ in range(n):
    set_n.add(input().rstrip())

for _ in range(m):
    set_m.add(input().rstrip())

result = set_n & set_m

print(len(result))

for i in sorted(list(result)):
    print(i)
