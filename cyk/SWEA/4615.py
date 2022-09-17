# 재미있는 오셀로 게임
# 돌의 색이 1이면 흑돌, 2이면 백돌
# 보드 위의 흑돌, 백돌의 개수를 출력
import sys
sys.stdin = open("sample_input(1).txt", "r")

T = int(input())
def check(row, col, color): # 위쪽 돌 판단

    for dR, dC in [[0,1],[0,-1],[1,0],[-1,0],[1,1],[-1,-1],[-1,1],[1,-1]]:
        nR = row+dR
        nC = col+dC
        cnt = 0
        checking = False
        while 0 <= nR < N and 0 <= nC < N:    #반대색인 경우
            cnt += 1
            if arr[nR][nC] == 0:
                break
            if arr[nR][nC] == color:
                checking = True
                break
            nR += dR
            nC += dC

        if checking:
            while cnt > 0:
                cnt -= 1
                nR = nR-dR
                nC = nC-dC
                arr[nR][nC] = color



for tc in range(1, 1+T):
    N, M = map(int, input().split())
    arr = [[0]*N for _ in range(N)]
    arr[N//2-1][N//2-1] = 2
    arr[N//2-1][N//2] = 1
    arr[N//2][N//2-1] = 1
    arr[N//2][N//2] = 2

    for _ in range(M):
        r, c, color = map(int, input().split())
        arr[r-1][c-1] = color
        check(r-1, c-1, color)
    res1, res2 = 0,0
    for lst in arr:
        res1 += lst.count(1)
        res2 += lst.count(2)
    print(f'#{tc} {res1} {res2}')