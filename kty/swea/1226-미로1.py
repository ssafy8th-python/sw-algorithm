import sys

sys.stdin = open("input_1226.txt", "r")


def dfs(sti, stj):
    st = []
    visited = [[0] * n for _ in range(n)]
    st.append((sti, stj))
    visited[sti][stj] = 1
    while st:
        i, j = st.pop()
        if miro[i][j] == 3:
            return 1
        for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            ni = i + di
            nj = j + dj
            if 0 <= ni < n and 0 <= nj < n and miro[ni][nj] != 1 and  not visited[ni][nj]:
                st.append((ni, nj))
                visited[ni][nj] = 1

    return 0

T = 10
for _ in range(1, T + 1):
    tc = int(input())
    n = 16
    miro = [list(map(int, input())) for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if miro[i][j] == 2:
                sti, stj = i, j

    print(f'#{tc} {dfs(sti, stj)}')

