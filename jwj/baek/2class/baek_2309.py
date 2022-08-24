def dfs(n, s):

    if n == 7 and s == 100:
        return 1
    else:
        for i in range(9):
            if visited[i] == 0:
                visited[i] = lst[i]
                res = dfs(n+1, s+lst[i])
                if res == 1:
                    return 1
                visited[i] = 0


lst = []

for _ in range(9):
    lst.append(int(input()))


visited = [0] * 9

dfs(0, 0)

visited.sort()

for i in range(2, 9):
    print(visited[i])
