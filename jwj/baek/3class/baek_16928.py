import sys
input = sys.stdin.readline


def select(position, cnt):
    global min_cnt

    if position >= 100:
        if min_cnt > cnt:
            min_cnt = cnt
        return

    if min_cnt <= cnt:
        return

    for i in range(0, 7):
        if move[position+i] != 0:

            tmp = move[position+i]

            move[position+i] = 0
            select(tmp, cnt+1)
            move[position+i] = tmp

    for i in range(6, 0, -1):
        if move[position+i] == 0:
            select(position+i, cnt+1)
            break


N, M = map(int, input().split())

move = [0] * 110        # 사다리 또는 뱀의 이동
min_cnt = 100
for _ in range(N+M):
    x, y = map(int, input().split())
    move[x] = y

select(1, 0)

print(min_cnt)
