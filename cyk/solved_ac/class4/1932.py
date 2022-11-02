# 정수 삼각형
import sys
input = sys.stdin.readline

N = int(input())
tri = []
for _ in range(N):
    ipt = list(map(int, input().split()))
    tri.append(ipt)

k = 2
for i in range(1, N):
    for j in range(k):
        if j == 0:
            tri[i][j] = tri[i][j] + tri[i-1][j]
        elif i == j:
            tri[i][j] = tri[i][j] + tri[i-1][j-1]
        else:
            tri[i][j] = max(tri[i-1][j-1], tri[i-1][j]) + tri[i][j]
    k += 1

print(max(tri[N-1]))
