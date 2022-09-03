# 듣보잡
import sys
input = sys.stdin.readline
N, M = map(int, input().split())

see = {input().rstrip() for _ in range(N)}
hear = {input().rstrip() for _ in range(M)}
res = see & hear
print(len(res))
for elem in sorted(res):
    print(elem)