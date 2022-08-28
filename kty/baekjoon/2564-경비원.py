def location(d, far):       # 좌표 구하기
    if d == 1:
        x = far
        y = h
    elif d == 2:
        x = far
        y = 0
    elif d == 3:
        x = 0
        y = h - far
    else:
        x = w
        y = h - far
    return x, y

w, h = map(int, input().split())
n = int(input())
shop = [list(map(int, input().split())) for _ in range(n)]
dong = list(map(int, input().split()))
# 1: 북쪽, 2: 남쪽, 3: 서쪽, 4: 동쪽
dx, dy = location(dong[0], dong[1])

minV = 0
for i in shop:
    minx = 0
    miny = 0
    x, y = location(i[0], i[1])

    if x + dx < (w-x) + (w-dx):         # x거리의 최소값은 두 개를 더한값과 w에서 빼고 더한 값중 하나이다.
        minx = x + dx
    else:
        minx = (w - x) + (w - dx)

    if y + dy < (h - y) + (h - dy):     # y거리의 최소값은 두 개를 더한값과 h에서 빼고 더한 값중 하나이다.
        miny = y + dy
    else:
        miny = (h - y) + (h - dy)

    if miny == 0:                       # 동근이랑 상점이랑 같은 라인에 있으면 거리의 차이가 곧 최솟값이 된다.
        minx = abs(x-dx)
    if minx == 0:
        miny = abs(y-dy)

    minV += (minx + miny)       # 상점과 동근이 사이의 거리의 최솟값을 더해준다.

print(minV)