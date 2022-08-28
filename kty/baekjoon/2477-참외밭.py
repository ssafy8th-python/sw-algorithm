import sys

n = int(sys.stdin.readline())
land = [list(map(int, sys.stdin.readline().split())) for _ in range(6)]

maxW = 0        # 가장 긴 세로 저장
maxH = 0        # 가장 긴 가로 저장
for i in range(6):
    if land[i][0] == 1 or land[i][0] == 2:      # 동쪽이나 서쪽일 때
        if land[i][1] > maxW:
            maxW = land[i][1]
            idx_W = i

    else:
        if land[i][1] > maxH:                   # 남쪽이나 북쪽일 때
            maxH = land[i][1]
            idx_H = i

lst = []                                        # 가장 긴변에 인접해 있는 변 2개 씩 총 4개를 저장
lst.append(land[idx_W-1])
lst.append(land[(idx_W+1) % 6])
lst.append(land[idx_H-1])
lst.append(land[(idx_H+1) % 6])

small = 1
for i in range(6):
    if land[i] not in lst:                      # 가장 긴변에 인접해 있는 변들이 아니면 작은 사각형을 이루는 변
        small *= land[i][1]                     # 남아있는 변 2개를 곱한다.

print((maxW*maxH-small)*n)                      # 큰 사각형에서 작은 사각형 뺴주기
