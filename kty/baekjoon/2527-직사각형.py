import sys

sys.stdin = open("2527.txt", "r")

def check(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
    if ax2 < bx1 or bx2 < ax1 or by2 < ay1 or ay2 < by1:        # 만나지 않을 경우
        return 'd'
    elif ax2 == bx1 or ax1 == bx2:
        if ay2 == by1 or ay1 == by2:        # 한 점에서 만날 경우
            return 'c'
        else:                               # 선으로 만날 경우
            return 'b'
    elif ay2 == by1 or ay1 == by2:          # 선으로 만날 경우
        return 'b'
    else:               # 겹칠 경우
        return 'a'

for _ in range(4):
    ax1, ay1, ax2, ay2, bx1, by1, bx2, by2 = map(int, input().split())
    print(check(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2))
