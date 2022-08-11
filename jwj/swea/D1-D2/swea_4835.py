T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    lst = list(map(int, input().split()))

    maxV = 0
    minV = 1000000

    i = 0

    while i <= N - M :
        min_sum = 0
        max_sum = 0
        for idx in range(i, M+i):
            min_sum += lst[idx]
            max_sum += lst[idx]

        if min_sum < minV:
            minV = min_sum

        if max_sum > maxV:
            maxV = max_sum

        i += 1

    print(f'#{tc} {maxV-minV}')
