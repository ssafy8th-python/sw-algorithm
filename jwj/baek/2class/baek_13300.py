import math

N, K = map(int, input().split())

room = [[0, 0] for _ in range(7)]

result = 0

for i in range(N):
    S, Y = map(int, input().split())
    if S == 0:
        room[Y][0] += 1
    else:
        room[Y][1] += 1

for i in range(1, 7):
    result += math.ceil(room[i][0] / K)
    result += math.ceil(room[i][1] / K)

print(result)
