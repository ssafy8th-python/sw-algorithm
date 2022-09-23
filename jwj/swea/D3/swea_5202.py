T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr = sorted(arr)

    start = arr[0][1]
    cnt = 1
    for s, e in arr[1:]:
        if start <= s:
            cnt += 1
            start = e
        elif start > e:
            start = e

    print(f'#{test_case} {cnt}')
