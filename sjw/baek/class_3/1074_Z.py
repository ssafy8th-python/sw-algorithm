# 1074 Z
# 주소: https://www.acmicpc.net/problem/1074

# 제출한 답
import sys
input = sys.stdin.readline


# 범위안에 안들면 (er - sr) * (ec - sc) 만큼 cnt에 더하고 return
def Z(sr, er, sc, ec):
    global cnt, result
    if not sr <= r <= er or not sc <= c <= ec:
        cnt += (er - sr) * (ec - sc)
        return
    if result:
        return

    if (er - sr) == 1:
        cnt += 1
        if sr == r and sc == c:
            result += cnt
        return

    rmid = (er + sr) // 2
    cmid = (ec + sc) // 2

    Z(sr, rmid, sc, cmid)
    Z(sr, rmid, cmid, ec)
    Z(rmid, er, sc, cmid)
    Z(rmid, er, cmid, ec)


N, r, c = map(int, input().split())
cnt, result = -1, 0

Z(0, 2 ** N, 0, 2 ** N)
print(result)