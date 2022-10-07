from collections import deque
from copy import deepcopy


def can_air(lst, start_x, start_y):
    q = deque()
    q.append((start_x, start_y))
    lst[start_x][start_y] = True

    while q:
        cur_x, cur_y = q.popleft()

        for d_x, d_y in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            n_x = cur_x + d_x
            n_y = cur_y + d_y
            if 0 <= n_x < N and 0 <= n_y < M and not lst[n_x][n_y] and not cheese[n_x][n_y]:
                lst[n_x][n_y] = True
                q.append((n_x, n_y))


def remove_cheese(cheese_num, air):

    result = 0
    while cheese_num != 0:
        # 초기 접촉가능한 공기 판별
        tmp_air = deepcopy(air)

        for i in range(N):
            for j in range(M):
                # 치즈가 있을 때
                if cheese[i][j]:
                    # 접촉한 공기의 수
                    cnt = 0
                    for d_x, d_y in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        n_x = i + d_x
                        n_y = j + d_y
                        if 0 <= n_x < N and 0 <= n_y < M and air[n_x][n_y]:
                            cnt += 1
                    if cnt >= 2:
                        cheese_num -= 1
                        cheese[i][j] = 0
                        can_air(tmp_air, i, j)

        air = deepcopy(tmp_air)
        result += 1
    return result


N, M = map(int, input().split())

cheese = [list(map(int, input().split())) for _ in range(N)]

# 치즈의 개수
cheese_num = 0

for c in cheese:
    s = sum(c)
    cheese_num += s

# 접촉 가능한 공기 판별
air = [[False] * M for _ in range(N)]

can_air(air, 0, 0)

result = remove_cheese(cheese_num, air)

print(result)

