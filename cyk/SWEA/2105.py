# 디저트 카페
import sys
sys.stdin = open("sample_input (3).txt","r")

def solve(k, r, c, d):
    global maxV
    if d == 3 and r == stR and c == stC:
        # print(result[:k])

        if maxV < k:
            maxV = k
        return

    if r >= n or c >= n or r < 0 or c < 0 or arr[r][c] in result[:k]:
        # r과 c가 범위를 벗어나거나 같은 디저트면:
        return

    if d == 2 and maxV >= k*2:
        return
    
    result[k] = arr[r][c]
    newR, newC = r+dR[d], c+dC[d]
    solve(k+1, newR, newC, d)
    d = (d+1)%4
    newR, newC = r+dR[d], c+dC[d]
    solve(k+1, newR, newC, d)


T = int(input())
for tc in range(1, 1+T):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    dR = [1, 1, -1, -1]
    dC = [1, -1, -1, 1]
    maxV =0
    for r in range(n):
        for c in range(n):
            stR, stC = r, c
            # result = [(r, c)]
            result = [-1]*(4*n)
            # desertLst = [arr[r][c]]
            solve(0, r, c, 0)
    print(f'#{tc}', end=" ")
    if maxV:
        print(maxV)
    else:
        print(-1)
