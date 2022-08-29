import sys

sys.stdin = open("2578.txt", "r")


def check(brd):                     # 빙고 수 체크
    diag_l = []                     # 가로, 세로, 가로 대각선, 세로 대각선 리스트를 만들어서,
    diag_r = []                     # 각 행열마다 추가 해주고 0이 5개면 빙고값에 1씩 더해 줌
    bingo = 0
    for i in range(5):
        garo = []
        sero = []
        for j in range(5):
            garo.append(brd[i][j])
            sero.append(brd[j][i])
            if i == j:
                diag_l.append(brd[i][j])
            if i + j == 4:
                diag_r.append(brd[i][j])

        if garo.count(0) == 5:
            bingo += 1
        if sero.count(0) == 5:
            bingo += 1
    if diag_l.count(0) == 5:
        bingo += 1
    if diag_r.count(0) == 5:
        bingo += 1
    return bingo

def play():
    for n in range(len(call)):
        for i in range(5):
            for j in range(5):
                if call[n] == brd[i][j]:    # 사회자가 부른 값에 해당 하는 보드판 숫자를 0으로 바꿈
                    brd[i][j] = 0
                    if check(brd) >= 3:     # 빙고 수 체크
                        return n

brd = [list(map(int, input().split())) for _ in range(5)]
call = []
for _ in range(5):
    call += list(map(int, input().split()))

print(play()+1)

