T = int(input())

for tc in range(1, T+1):
    D, A, B = map(int, input().split())
    D = str(D)

    result = [True] * (B + 1)
    result[0] = False
    result[1] = False
    cnt = 0

    prime = 2

    while prime * prime < B:
        for i in range(prime, B+1, prime):
            result[i] = False

        result[prime] = True

        for i in range(prime+1, B+1):
            if result[i]:
                prime = i
                break

    for idx in range(A, B+1):
        if result[idx]:
            idx_str = str(idx)
            for char in idx_str:
                if D == char:
                    cnt += 1
                    break

    print(f'#{tc} {cnt}')

