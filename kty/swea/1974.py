import sys

sys.stdin = open("input_1974.txt", "r")

def sudoku(sudo):
    for i in range(9):
        stack_row = set()
        stack_col = set()
        for j in range(9):
            stack_row.add(sudo[i][j])
            stack_col.add(sudo[j][i])
        if len(stack_row) < 9 or len(stack_col) < 9:
            return '0'

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            stack_block = set()
            for r_p in range(0, 3):
                for c_p in range(0, 3):
                    stack_block.add(sudo[i+r_p][j+c_p])
        if len(stack_block) < 9:
            return '0'

    return '1'

T = int(input())

for tc in range(1, T + 1):
    sudo = [list(map(int, input().split())) for _ in range(9)]

    print(f'#{tc} {sudoku(sudo)}')

