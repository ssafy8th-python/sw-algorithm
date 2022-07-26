def dfs(cnt, position):
    global square, N
    square[position[0]][position[1]] = 0

    for x in [-1, 1]:
        if position[1]+x <N and -1 < position[1]+x and square[position[0]][position[1]+x] == 1:
            cnt = dfs(cnt+1, [position[0], position[1]+x])
    for y in [-1, 1]:
        if position[0]+y <N and -1 < position[0]+y and square[position[0]+y][position[1]] == 1:
            cnt = dfs(cnt+1, [position[0]+y, position[1]])
    return cnt


N = int(input())

square = []

for _ in range(N):
    square += [list(map(int, list(input())))]

result = []

for i in range(N):
    for j in range(N):
        if square[i][j] == 1:
            result += [dfs(1, [i, j])]

result.sort()
print(len(result))
for num in result:
    print(num)