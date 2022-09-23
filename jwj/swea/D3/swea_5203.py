T = int(input())

for test_case in range(1, T + 1):
    arr = list(map(int, input().split()))

    player1 = [0] * 13
    player2 = [0] * 13

    for idx in range(0, len(arr), 2):
        player1[arr[idx]] += 1
        player2[arr[idx+1]] += 1

        result = 0
        if idx >= 4:
            for i in range(10):
                if player1[i] >= 3:
                    result = 1
                    break

                tmp = bool(player1[i]) + bool(player1[i + 1]) + bool(player1[i + 2])
                if tmp >= 3:
                    result = 1
                    break

            if result:
                break

            for i in range(10):
                if player2[i] >= 3:
                    result = 2
                    break

                tmp = bool(player2[i]) + bool(player2[i+1]) + bool(player2[i+2])
                if tmp >= 3:
                    result = 2
                    break

            if result:
                break

        if result:
            break

    print(f'#{test_case} {result}')
