T = int(input())

for tc in range(1, T+1):
    K, N, M = map(int, input().split())

    M_lst = map(int, input().split())
    count_lst = [0] * 103

    for num in M_lst:
        count_lst[num] = 1

    result = 0
    current = 0

    while current < N:

        for i in range(current + K, current, -1):
            if i >= N:
                current = N
                break

            if count_lst[i] == 1:
                current = i
                result += 1
                break

        else:
            result = 0
            break

    print(f'#{tc} {result}')

