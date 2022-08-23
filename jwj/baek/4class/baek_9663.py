N = int(input())


def is_ok(row):

    # 세로 확인, 대각선 확인
    for i in range(row):
        if visited[row] == visited[i] or abs(visited[row] - visited[i]) == abs(row - i):
            return False

    return True


def dfs(k):
    global result

    if k == N:
        result += 1
    else:
        for i in range(N):
            visited[k] = i
            if is_ok(k):
                dfs(k+1)


result = 0
visited = [0] * N
dfs(0)

print(result)
