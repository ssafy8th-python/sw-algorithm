T = int(input())

for test_case in range(1, T+1):
    N = int(input())

    omok = [input() for _ in range(N)]

    check = False

    for i in range(N):
        width = 0
        vertical = 0
        for j in range(N):
            if omok[i][j] == 'o':
                width += 1
            else:
                width = 0

            if omok[j][i] == 'o':
                vertical += 1
            else:
                vertical = 0

            if omok[i][j] == 'o':
                diagonal = 1
                n_i, n_j = i + 1, j + 1

                while n_i < N and n_j < N and omok[n_i][n_j] == 'o':
                    diagonal += 1
                    n_i += 1
                    n_j += 1

                    if diagonal == 5:
                        check = True
                        break

                diagonal = 1
                n_i, n_j = i + 1, j - 1

                while n_i < N and 0 <= n_j and omok[n_i][n_j] == 'o':
                    diagonal += 1
                    n_i += 1
                    n_j -= 1

                    if diagonal == 5:
                        check = True
                        break

            if width == 5 or vertical == 5:
                check = True
                break

        if check:
            break

    if check:
        print(f'#{test_case} YES')
    else:
        print(f'#{test_case} NO')


