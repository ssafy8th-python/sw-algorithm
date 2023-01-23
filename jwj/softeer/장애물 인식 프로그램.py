def dfs(blocks, i, j, visited):
    global value
    if i < 0 or i >= N or j < 0 or j >= N:
        return False

    if blocks[i][j] == "1" and not visited[i][j]:
        visited[i][j] = 1
        value += 1
        dfs(blocks, i + 1, j, visited)
        dfs(blocks, i - 1, j, visited)
        dfs(blocks, i, j + 1, visited)
        dfs(blocks, i, j - 1, visited)
        return True

    return False


N = int(input())
blocks = []

for i in range(N):
    blocks.append(list(input()))

visited = [[0] * N for _ in range(N)]

value = 0
result = []

# dfs 이용하여 장애물을 모두 저장
for i in range(N):
    for j in range(N):
        # 장애물 확인
        if dfs(blocks, i, j, visited):
            result.append(value)
            value = 0

result.sort()
print(len(result))
for re in result:
    print(re)



