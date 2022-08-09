T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))

    max = lst[0]
    min = lst[0]

    for num in lst:
        if max < num:
            max = num

        if min > num:
            min = num

    print(f'#{test_case} {max - min}')
