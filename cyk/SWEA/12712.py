# 델타로 다시 코드 고치기 !
# import sys
# sys.stdin = open("in1.txt", "r")
#
# T = int(input())
#
# for tc in range(1, T+1):
#     N ,M = map(int, input().split())
#     fly = [list(map(int, input().split())) for _ in range(N)] # N*N 판
#     sum_kill = []
#
#
#     for i in range(N):
#         for j in range(N):
#             lst1 = [[fly[i][j]]]
#             for x in range(1, M):
#                 sumV = 0
#                 if i-x < 0:
#                     a = []
#                 else:
#                     a = fly[i-x][j]
#                 if i+x > N-1:
#                     b = []
#                 else:
#                     b = fly[i+x][j]
#                 if j+x > N-1:
#                     c = []
#                 else:
#                     c = fly[i][j+x]
#                 if j - x < 0:
#                     d = []
#                 else:
#                     d = fly[i][j-x]
#                 check1 = [a,b,c,d]
#                 lst1.append(check1)
#                 for check in lst1:
#                     for elem in check:
#                         if elem:
#                             sumV += elem
#                 sum_kill.append(sumV)
#
#     for i in range(N):
#         for j in range(N):
#             lst2=[[fly[i][j]]]
#             for x in range(1, M):
#                 sumV = 0
#                 if i-x < 0 or j-x < 0:
#                     a = []
#                 else:
#                     a = fly[i-x][j-x]
#                 if i+x > N-1 or j+x > N-1:
#                     b = []
#                 else:
#                     b = fly[i+x][j+x]
#                 if i-x < 0 or j+x> N-1:
#                     c = []
#                 else:
#                     c = fly[i-x][j+x]
#                 if j - x < 0 or  i+x > N-1:
#                     d = []
#                 else:
#                     d = fly[i+x][j-x]
#                 check2 = [a,b,c,d]
#                 lst2.append(check2)
#                 for check in lst2:
#                     for elem in check:
#                         if elem:
#                             sumV += elem
#                 sum_kill.append(sumV)
#
#     print(f'#{tc} {max(sum_kill)}')


import sys
sys.stdin = open("in1.txt", "r")
T = int(input())
for tc in range(1, 1+T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    maxV = 0
    sumV = 0
    # 위, 아래, 왼쪽, 오른쪽
    dR = [-1, 1, 0, 0]
    dC = [0, 0, -1, 1]
    xR = [-1, 1, 1, -1]
    xC = [-1, 1, -1, 1]

    newR, newC = 0, 0

    for i in range(N):
        for j in range(N):
            sumV = arr[i][j]
            for k in range(4):  # plus 모양
                for t in range(1, M):
                    newR = i + dR[k] * t
                    newC = j + dC[k] * t
                    if 0 <= newR < N and 0 <= newC < N:
                        sumV += arr[newR][newC]

            if sumV > maxV:
                maxV = sumV

            sumV = arr[i][j]
            for k in range(4):  # X 모양
                for t in range(1, M):
                    newR = i + xR[k] * t
                    newC = j + xC[k] * t
                    if 0 <= newR < N and 0 <= newC < N:
                        sumV += arr[newR][newC]

            if sumV > maxV:
                maxV = sumV
    print(f'#{tc} {maxV}')