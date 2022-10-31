def ccw(x1, y1, x2, y2, x3, y3, x4, y4):
    f1 = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)
    f2 = (x2 - x1) * (y4 - y1) - (y2 - y1) * (x4 - x1)

    return f1 * f2


x1, y1, x2, y2 = map(int, input().split())

x3, y3, x4, y4 = map(int, input().split())

# 첫번째 선분을 기준으로
f1 = ccw(x1, y1, x2, y2, x3, y3, x4, y4)

# 두번째 선분을 기준으로
f2 = ccw(x3, y3, x4, y4, x1, y1, x2, y2)


if f1 == 0 and f2 == 0:
    if min(x1, x2) <= max(x3, x4) and min(x3, x4) <= max(x1, x2) \
            and min(y1, y2) <= max(y3, y4) and min(y3, y4) <= max(y1, y2):
        print(1)
    else:
        print(0)
elif f1 <= 0 and f2 <= 0:
    print(1)
else:
    print(0)




