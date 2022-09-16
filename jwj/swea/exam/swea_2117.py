costs = [0]

for k in range(1, 41):
    costs.append(k * k + (k - 1) * (k - 1))


def find(row, col):
    dis = [0] * (2 * N + 1)
    for hRow, hCol in homes:
        # 시작지점으로부터 home까지의 거리를 계산하여 (dis에 count)
        t = abs(hRow - row) + abs(hCol - col)
        dis[t] += 1
    maxNum = 0
    for k in range(1, 2 * N + 1):
        numH = sum(dis[:k])
        if numH * M - costs[k] >= 0 and maxNum < numH:
            maxNum = numH
    return maxNum


TC = int(input())
for test_case in range(1, TC + 1):
    N, M = map(int, input().split())
    city = [list(map(int, input().split())) for i in range(N)]
    homes = []
    maxV = 0
    for row in range(N):
        for col in range(N):
            if city[row][col] == 1:
                homes.append((row, col))
    for row in range(N):
        for col in range(N):
            result = find(row, col)
            if maxV < result:
                maxV = result
    print(f'#{test_case}', maxV)