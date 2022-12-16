board = [list(map(int, input().split())) for _ in range(9)]

max_value = 0
result = [1, 1]

for i in range(9):
    for j in range(9):
        if board[i][j] > max_value:
            max_value = board[i][j]
            result[0] = i + 1
            result[1] = j + 1

print(max_value)
print(result[0], result[1])