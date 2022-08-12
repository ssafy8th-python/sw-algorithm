T = int(input())

for tc in range(1, T+1):
    N = int(input())
    a = int(input())
    lst = [0] * 10

    while a != 0:
        lst[a % 10] += 1
        a //= 10

    maxV = 0

    for idx in range(9, -1, -1):
        if lst[maxV] < lst[idx]:
            maxV = idx

    print(f'#{tc} {maxV} {lst[maxV]}')
