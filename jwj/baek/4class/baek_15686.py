import sys

input = sys.stdin.readline


def dfs(c_num, begin):
    if c_num == M:
        visited_all.append(visited[::])
    else:
        for idx in range(begin, chicken_num):
            visited[c_num] = chicken[idx]
            dfs(c_num + 1, idx+1)


N, M = map(int, input().split())

city = [list(map(int, input().split())) for _ in range(N)]

house = []

chicken = []

chicken_num = 0

for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            house.append((i, j))
        elif city[i][j] == 2:
            chicken.append((i, j))
            chicken_num += 1

visited = [0] * M

visited_all = []

dfs(0, 0)

result = 10000

for chickens in visited_all:
    sumV = 0
    for h in house:
        minV = 100

        for c in chickens:
            uclid = abs(h[0] - c[0]) + abs(h[1] - c[1])

            if minV > uclid:
                minV = uclid

            if minV == 1:
                break

        sumV += minV

    result = min(result, sumV)

print(result)
