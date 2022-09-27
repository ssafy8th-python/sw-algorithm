# 1074 Z
# 주소: https://www.acmicpc.net/problem/1074

# 제출한 답
import sys
input = sys.stdin.readline


def Z(sr, er, sc, ec):
    global cnt, result
    if result:
        return

    if er - sr == 1:
        cnt += 1
        if sr == r and sc == c:
            result = cnt
        return

    mid = (er - 1 + sr) // 2
2 3 4 5
    Z(sr, mid, sc, mid)
    Z(sr, mid, mid, ec)
    Z(mid, er, sc, mid)
    Z(mid, er, mid, ec)


N, r, c = map(int, input().split())
board = [[0] * 2 ** N for _ in range(2 ** N)]
cnt, result = 0, 0

Z(0, 2 ** N, 0, 2 ** N)
print(result)


# 재귀로 나눠서 들가부리기
# 들가서 len이 1이면 cnt += 1
# r: [0:mid] [0:mid]
# c: [0:mid] [mid:N]

# r: [mid:N]  [mid:N]
# c: [0:mid] [mid:N]