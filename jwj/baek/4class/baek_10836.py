import sys
input = sys.stdin.readline

N, M = map(int, input().split())

bee = [[1] * N for _ in range(N)]

growth = [0] * (2 * N - 1)

for _ in range(M):
    z, o, t = list(map(int, input().split()))

    for i in range(z, z + o):
        growth[i] += 1

    for i in range(z + o, z + o + t):
        growth[i] += 2

index = 0
for i in range(N-1, -1, -1):
    bee[i][0] += growth[index]
    index += 1

for i in range(1, N):
    bee[0][i] += growth[index]
    index += 1


for i in range(1, N):
    for j in range(1, N):
        bee[i][j] = bee[0][j]

for b in bee:
    print(*b)
