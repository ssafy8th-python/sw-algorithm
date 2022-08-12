for tc in range(1, 11):
    N = int(input())
    box = list(map(int, input().split()))
    lst = [0] * 101

    minV = 101
    maxV = 0

    for num in box:
         lst[num] += 1

    for idx in range(101):
        if lst[idx] != 0:
            minV = idx
            break

    for idx in range(100, -1, -1):
        if lst[idx] != 0:
            maxV = idx
            break

    for i in range(N):

        if maxV <= minV:
            print(tc)
            break

        lst[maxV] -= 1
        lst[maxV-1] += 1

        lst[minV] -= 1
        lst[minV+1] += 1

        if not lst[maxV]:
            while True:
                maxV -= 1
                if lst[maxV]:
                    break

        if not lst[minV]:
            while True:
                minV += 1
                if lst[minV]:
                    break

    print(f'#{tc} {maxV-minV}')
