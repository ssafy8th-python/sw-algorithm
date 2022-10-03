T = int(input())


def swim(m, v):
    global minV

    if m >= 12:
        if minV > v:
            minV = v
    else:
        if month[m] == 0:
            swim(m+1, v)
        else:
            swim(m+1, v + (one * month[m]))
            swim(m+1, v + m1)
            swim(m+3, v + m3)


for test_case in range(1, T+1):
    one, m1, m3, y = map(int, input().split())

    month = list(map(int, input().split()))

    minV = y

    swim(0, 0)

    print(f'#{test_case} {minV}')
