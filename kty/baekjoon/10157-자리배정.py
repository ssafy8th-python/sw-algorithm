import sys

c, r = map(int, sys.stdin.readline().split())
k = int(sys.stdin.readline())

def wait(world):
    di = [0, 1, 0, -1]                  # 오, 아, 왼, 위
    dj = [1, 0, -1, 0]

    cnt = 1                             # 대기 번호
    i = j = d = 0
    if k -1 >= r * c:                   # 대기 번호가 좌석수를 넘는 손님이 오면 0 반환
        return 0
    for _ in range(k-1):
        world[i][j] = cnt
        cnt += 1
        ni = i + di[d]
        nj = j + dj[d]
        if ni < 0 or ni >= c or nj < 0 or nj >= r or world[ni][nj] != 0:
            d = (d+1) % 4
        i = i + di[d]
        j = j + dj[d]
    return f'{i+1} {j+1}'                   # 0, 0 부터 시작해서 1씩 더해줌

world = [[0] * r for _ in range(c)]         # 옆으로 돌려서 진행

print(wait(world))

