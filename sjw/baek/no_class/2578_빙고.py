# 2578 빙고
# 주소: https://www.acmicpc.net/problem/2578

# 제출한 답
# import sys
# input = sys.stdin.readline


def check():
    for num in range(25):
        for r in range(5):
            for c in range(5):
                if bingo_board[r][c] == call[num]:
                    bingo_board[r][c] = 0
                    bingo = 0
                    cnt_lb = 0; cnt_rb = 0
                    for i in range(5):
                        cnt_r = 0; cnt_c = 0
                        for j in range(5):
                            if bingo_board[i][j] == 0:
                                cnt_r += 1
                                if cnt_r == 5:
                                    bingo += 1
                            if bingo_board[j][i] == 0:
                                cnt_c += 1
                                if cnt_c == 5:
                                    bingo += 1
                            if i == j and bingo_board[i][j] == 0:
                                cnt_rb += 1
                                if cnt_rb == 5:
                                    bingo += 1
                            if i + j == 4 and bingo_board[i][j] == 0:
                                cnt_lb += 1
                                if cnt_lb == 5:
                                    bingo += 1
                    if bingo >= 3:
                        return num + 1
                    break
            else:
                continue
            break


bingo_board = [list(map(int, input().split())) for _ in range(5)]
call = []

for _ in range(5):
    tmp = list(map(int, input().split()))
    for u in tmp:
        call.append(u)

print(check())


# 다른 답
def check():
    dt = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    bingo = 0
    for num in range(25):
        for r in range(5):
            for c in range(5):
                if bingo_board[r][c] == call[num]:
                    bingo_board[r][c] = 0
                    for pr, pc in dt:
                        cnt = 1
                        for dis in range(1, 5):
                            nr = r + pr * dis
                            nc = c + pc * dis
                            if 0 <= nr < 5 and 0 <= nc < 5 and bingo_board[nr][nc] == 0:
                                cnt += 1
                        if cnt == 5:
                            bingo += 1
                    break
            else:
                continue
            break
        if bingo >= 3:
            return num + 1


bingo_board = [list(map(int, input().split())) for _ in range(5)]
call = []

for _ in range(5):
    tmp = list(map(int, input().split()))
    for i in tmp:
        call.append(i)

print(check())
