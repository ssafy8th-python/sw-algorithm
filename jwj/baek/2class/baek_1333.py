import math

# 곡, 노래 길이, 벨 시간
N, L, D = map(int, input().split())

time = 0
res = 0
# 노래 N 곡
for _ in range(N):

    # 노래 부르는 중
    time += L

    # 노래 끝남 5초 간 조용한 구간
    for t in range(time, time + 5):
        if t % D == 0:
            res = t
            break

    if res:
        break

    # 휴식시간
    time += 5
else:
    res = math.ceil(time / D) * D

print(res)