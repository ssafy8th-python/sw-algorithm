T = int(input())

for tc in range(1, T+1):
    N = list(map(int, input()))

    N_length = len(N)

    result = [0] * N_length

    cnt = 0

    for i in range(0, N_length):
        if result[i] != N[i]:
            cnt += 1
            num = N[i]
            for j in range(i, N_length):
                result[j] = num

    print(f'#{tc} {cnt}')
