# 홈 방범 서비스
import sys
sys.stdin = open("sample_input (3).txt", "r")
'''
1
7 7
0 0 0 1 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
1 0 0 0 0 0 1
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 1 0 0 0
'''
# 운영 비용 = K*K + (K-1)*(K-1)
# 운영 영역의 크기 K는 1 이상의 정수
# 손해보지 않으면서 홈방범 서비스를 가장 많은 집들에 제공하는 서비스 영역을 찾을 때 서비스를 제공받는 집들의 수
def find(row, col):
    dis = [0] * (2*N+1)
    for hRow, hCol in HOMES:
        t = abs(hRow-row) +abs(hCol-col)
        dis[t] += 1
    maxNum = 0
    for k in range(1, 2*N+1):
        numH = sum(dis[:k])
        if numH * M - (k*k +(k-1)*(k-1)) >= 0 and maxNum < numH:
            maxNum = numH
    return maxNum
T = int(input())
for tc in range(1, 1+T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    HOMES = []
    maxV =0

    for r in range(N):
        for c in range(N):
            if arr[r][c] == 1:
                HOMES.append((r, c))

    for row in range(N):
        for col in range(N):
            result = find(row, col)
            if maxV < result:
                maxV = result
    print(f'#{tc} {maxV}')