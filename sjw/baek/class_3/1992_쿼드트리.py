# 1992 쿼드트리
# 주소: https://www.acmicpc.net/problem/1992

import sys
input = sys.stdin.readline


def quad(rs, re, cs, ce):
    rmid, cmid = (rs + re) // 2, (cs + ce) // 2
    max_one = (rmid - rs + 1) ** 2
    print('(', end='')
    # 좌상
    cnt = 0
    for r in range(rs, rmid + 1):
        for c in range(cs, cmid + 1):
            if video[r][c]:
                cnt += 1
    if cnt == max_one:
        print('1', end='')
    elif not cnt:
        print('0', end='')
    else:
        quad(rs, rmid, cs, cmid)

    # 우상
    cnt = 0
    for r in range(rs, rmid + 1):
        for c in range(cmid + 1, ce + 1):
            if video[r][c]:
                cnt += 1
    if cnt == max_one:
        print('1', end='')
    elif not cnt:
        print('0', end='')
    else:
        quad(rs, rmid, cmid + 1, ce)

    # 좌하
    cnt = 0
    for r in range(rmid + 1, re + 1):
        for c in range(cs, cmid + 1):
            if video[r][c]:
                cnt += 1
    if cnt == max_one:
        print('1', end='')
    elif not cnt:
        print('0', end='')
    else:
        quad(rmid + 1, re, cs, cmid)

    # 우하
    cnt = 0
    for r in range(rmid + 1, re + 1):
        for c in range(cmid + 1, ce + 1):
            if video[r][c]:
                cnt += 1
    if cnt == max_one:
        print('1', end='')
    elif not cnt:
        print('0', end='')
    else:
        quad(rmid + 1, re, cmid + 1, ce)
    print(')', end='')


N = int(input())
video = [list(map(int, list(input().rstrip()))) for _ in range(N)]

cnt = 0
for r in range(N):
    for c in range(N):
        if video[r][c]:
            cnt += 1
if cnt == N * N:
    print(1)
elif not cnt:
    print(0)
else:
    quad(0, N - 1, 0, N - 1)


# 다른 답
import sys
input = sys.stdin.readline


def compression(n: int, start_r: int, start_c: int) -> str:
    if n == 1:
        return image[start_r][start_c]
    required = False
    target = image[start_r][start_c]
    for r in range(start_r, start_r + n):
        for c in range(start_c, start_c + n):
            if image[r][c] != target:
                required = True
                break
    if required:
        expression = '('
        expression += compression(n // 2, start_r, start_c)
        expression += compression(n // 2, start_r, start_c + n // 2)
        expression += compression(n // 2, start_r + n // 2, start_c)
        expression += compression(n // 2, start_r + n // 2, start_c + n // 2)
        expression += ')'
        return expression
    else:
        return target


n = int(input())
image = [list(input().rstrip()) for _ in range(n)]
print(compression(n, 0, 0))