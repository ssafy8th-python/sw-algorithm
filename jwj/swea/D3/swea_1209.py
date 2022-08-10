for tc in range(10):
    test_case = int(input())

    arr = [list(map(int, input().split())) for _ in range(100)]

    result = angleV = reAngleV = 0

    for i in range(100):
        rowV = colV = 0

        for j in range(100):
            rowV += arr[i][j]
            colV += arr[j][i]

        angleV += arr[i][j]
        reAngleV += arr[i][100-i-1]

        result = max(result, rowV, colV)

    result = max(result, angleV, reAngleV)

    print(f'#{test_case} {result}')
