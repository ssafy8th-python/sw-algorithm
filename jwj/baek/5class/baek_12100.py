import copy


def dfs(board, cnt):
    global max_value

    if cnt == 5:
        for b in board:
            max_value = max(max_value, max(b))
        return

    # 위
    tmp_board = copy.deepcopy(board)
    for i in range(N):
        top = 0
        for j in range(1, N):
            if tmp_board[j][i]:
                tmp = tmp_board[j][i]
                tmp_board[j][i] = 0

                if tmp_board[top][i] == 0:
                    tmp_board[top][i] = tmp
                elif tmp_board[top][i] == tmp:
                    tmp_board[top][i] = tmp * 2
                    top += 1
                else:
                    top += 1
                    tmp_board[top][i] = tmp

    dfs(tmp_board, cnt + 1)

    # 오른쪽
    tmp_board = copy.deepcopy(board)
    for i in range(N):
        top = N - 1
        for j in range(N-2, -1, -1):
            if tmp_board[i][j]:

                tmp = tmp_board[i][j]
                tmp_board[i][j] = 0

                if tmp_board[i][top] == 0:
                    tmp_board[i][top] = tmp
                elif tmp_board[i][top] == tmp:
                    tmp_board[i][top] = tmp * 2
                    top -= 1
                else:
                    top -= 1
                    tmp_board[i][top] = tmp

    dfs(tmp_board, cnt + 1)

    # 아래
    tmp_board = copy.deepcopy(board)
    for i in range(N):
        top = N - 1
        for j in range(N-2, -1, -1):
            if tmp_board[j][i]:

                tmp = tmp_board[j][i]
                tmp_board[j][i] = 0

                if tmp_board[top][i] == 0:
                    tmp_board[top][i] = tmp
                elif tmp_board[top][i] == tmp:
                    tmp_board[top][i] = tmp * 2
                    top -= 1
                else:
                    top -= 1
                    tmp_board[top][i] = tmp

    dfs(tmp_board, cnt + 1)

    # 왼쪽
    tmp_board = copy.deepcopy(board)
    for i in range(N):
        top = 0
        for j in range(1, N):
            if tmp_board[i][j]:

                tmp = tmp_board[i][j]
                tmp_board[i][j] = 0

                if tmp_board[i][top] == 0:
                    tmp_board[i][top] = tmp
                elif tmp_board[i][top] == tmp:
                    tmp_board[i][top] = tmp * 2
                    top += 1
                else:
                    top += 1
                    tmp_board[i][top] = tmp

    dfs(tmp_board, cnt + 1)


N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]

max_value = 0

dfs(board, 0)

print(max_value)