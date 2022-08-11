T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cnt_sort = [0] * 101
    a_lst = list(map(int, input().split()))
    result_lst = [0] * N

    for num in a_lst:
        cnt_sort[num] += 1

    for idx in range(1, 101):
        cnt_sort[idx] += cnt_sort[idx-1]

    for num in a_lst:
        result_lst[cnt_sort[num]-1] = num
        cnt_sort[num] -= 1

    print(f'#{tc}', end=' ')

    for idx in range(5):
        print(f'{result_lst[(idx+1)*-1]} {result_lst[idx]}', end=' ')
    print()
