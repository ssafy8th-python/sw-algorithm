# 1018 체스판 다시 칠하기
# 주소: https://www.acmicpc.net/problem/1018

# 제출한 답
# 1. 8 X 8로 자르기

# 2. 자른 것에서 몇개 색칠해야하는지 세서 해결

# 3. 가장 작은 값 출력

N, M = map(int, input().split())

board = []
count_lst = []
w = 'WBWBWBWB'
b = 'BWBWBWBW'

for _ in range(N):
    board.append(input())

for r_line in range(N-7):
    for c_line in range (M-7):
        temp_board = []
        for i in range(8):
            temp_board.append(board[r_line + i][c_line:c_line + 8])

        count = 0
        for line in range(8):
            if line % 2 == 0:
                if temp_board[line] != w:
                    for B_color, origin_color in zip(temp_board[line], w):
                        if B_color != origin_color:
                            count += 1
            elif line % 2:
                if board[line] != b:
                    for B_color, origin_color in zip(temp_board[line], b):
                        if B_color != origin_color:
                            count += 1
        count_lst.append(count)

        count = 0
        for line in range(8):
            if line % 2 == 0:
                if temp_board[line] != b:
                    for B_color, origin_color in zip(temp_board[line], b):
                        if B_color != origin_color:
                            count += 1
            elif line % 2:
                if temp_board[line] != w:
                    for B_color, origin_color in zip(temp_board[line], w):
                        if B_color != origin_color:
                            count += 1
        count_lst.append(count)
count_lst.sort()

print(count_lst[0])



