T = int(input())

lst = list(range(12))

for tc in range(1, T+1):
    N, K = map(int, input().split())
    result = 0
    for i in range(1 << 12):
        cnt = 0
        tmp = []
        sumV = 0
        for j in lst:
            if i & (1 << j):
                tmp.append(j)
                cnt += 1

            if cnt > N:
                break

        else:
            if cnt == N:
                for num in tmp:
                    sumV += num+1

                if sumV == K:
                    result += 1

    print(f'#{tc} {result}')
