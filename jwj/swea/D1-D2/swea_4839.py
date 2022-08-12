def search(start, end, target, cnt):

    while start <= end:
        cnt += 1
        mid = int((start + end) / 2)

        if mid == target:
            return cnt

        elif mid > target:
            end = mid

        else:
            start = mid

    return cnt


T = int(input())

for tc in range(1, T+1):
    P, A, B = map(int, input().split())

    A_cnt = search(1, P, A, 0)

    B_cnt = search(1, P, B, 0)

    result = 0

    if A_cnt < B_cnt:
        result = 'A'
    elif A_cnt > B_cnt:
        result = 'B'

    print(f'#{tc} {result}')
