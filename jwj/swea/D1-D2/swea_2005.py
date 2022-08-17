T = int(input())

for TC in range(1, T+1):
    N = int(input())

    dp = [[1]]

    for i in range(N-1):    # N = 2일 때
        dpTemp = [1]

        for j in range(i):
            dpTemp.append(dp[-1][j] + dp[-1][j+1])
        dpTemp.append(1)
        dp.append(dpTemp)

    print(f'#{TC}')
    for nums in dp:
        for num in nums:
            print(num, end=' ')
        print()

