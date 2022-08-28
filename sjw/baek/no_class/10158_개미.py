# 10158 개미
# 주소: https://www.acmicpc.net/problem/10158

# 제출한 답
import sys
input = sys.stdin.readline


def check():
    global x
    global y
    xt = t % (w * 2)
    yt = t % (h * 2)
    if ((x + xt) // w) % 2:
        x = w - ((x + xt) % w)
    else:
        x = (x + xt) % w

    if ((y + yt) // h) % 2:
        y = h - ((y + yt) % h)
    else:
        y = (y + yt) % h

    return [x, y]


w, h = map(int, input().split())
x, y = map(int, input().split())
t = int(input())

print(*check())
