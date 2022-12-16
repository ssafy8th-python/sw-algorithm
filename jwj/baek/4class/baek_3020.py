import sys
input = sys.stdin.readline

N, H = map(int, input().split())

cave_up = [0] * (H + 1)
cave_down = [0] * (H + 1)

for i in range(N):
    c = int(input())

    # 위
    if i % 2:
        cave_up[c] += 1

    # 아래
    else:
        cave_down[c] += 1

cave = [0] * (H + 1)

# 큰 장애물부터 계산
tmp = 0
for i in range(H, 0, -1):
    # 이전 더 큰 장애물의 값 더해서 다음 장애물에 추가
    tmp += cave_up[i]
    cave[i] += tmp

tmp = 0
for i in range(1, H+1):
    # 위에서부터 시작할 때이기 때문에 i와 장애물의 시작 위치를 반대로 수정정
    tmp += cave_down[H-i+1]
    cave[i] += tmp

min_v = min(cave[1:])
print(min_v, cave[1:].count(min_v))