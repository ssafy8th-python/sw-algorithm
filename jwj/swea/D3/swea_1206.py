for test_case in range(1, 11):
    N = int(input())

    apt = list(map(int, input().split()))
    cnt = 0

    for i in range(2, N-2):
        max_value = apt[i-2]
        tmp_lst = [apt[i-1], apt[i+1], apt[i+2]]

        for idx in range(3):
            if tmp_lst[idx] > max_value:
                max_value = tmp_lst[idx]

        if apt[i] > max_value:
            cnt += apt[i] - max_value

    print(f'#{test_case} {cnt}')
