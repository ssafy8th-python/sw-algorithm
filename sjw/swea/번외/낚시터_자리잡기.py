# No. 1 [연습문제] 낚시터 자리잡기
# 주소: https://swexpertacademy.com/main/talk/codeBattle/problemDetail.do?contestProbId=AYLNTUm6AswDFASv&categoryId=AYLNSmY6An0DFASv&categoryType=BATTLE&battleMainPageIndex=1

import sys
sys.stdin = open("input.txt", "r")


T = int(input())

for test_case in range(1, T + 1):
    n = int(input())  # 낚시터 자리의 개수
    position = [0] * (n + 1)  # 낚시터
    gates = [list(map(int, input().split())) for _ in range(3)]  # 게이트위치와 사람 수
    gates.sort()  # 게이트 정렬
    print(gates)
    result = 0
    # 가운데 먼저
    for i in range(gates[1][1]):
        for j in range(n):
            if gates[0][1] >= gates[2][1]:
                if 0 < gates[1][0] + j <= n:
                    if position[gates[1][0] + j] == 0:
                        position[gates[1][0] + j] += j + 1
                        break
                if 0 < gates[1][0] - j <= n:
                    if position[gates[1][0] - j] == 0:
                        position[gates[1][0] - j] += j + 1
                        break
            elif gates[0][1] < gates[2][1]:
                if 0 < gates[1][0] - j <= n:
                    if position[gates[1][0] - j] == 0:
                        position[gates[1][0] - j] += j + 1
                        break
                if 0 < gates[1][0] + j <= n:
                    if position[gates[1][0] + j] == 0:
                        position[gates[1][0] + j] += j + 1
                        break
    # 더 큰 것
    if gates[0][1] <= gates[2][1]:
        # 좌가 더 작음
        for i in range(gates[0][1]):
            for j in range(n):
                if 0 < gates[0][0] + j <= n:
                    if position[gates[0][0] + j] == 0:
                        position[gates[0][0] + j] += j + 1
                        break
                if 0 < gates[0][0] - j <= n:
                    if position[gates[0][0] - j] == 0:
                        position[gates[0][0] - j] += j + 1
                        break
        # 우가 더 큼
        for i in range(gates[2][1]):
            for j in range(n):
                if 0 < gates[2][0] + j <= n:
                    if position[gates[2][0] + j] == 0:
                        position[gates[2][0] + j] += j + 1
                        break
                if 0 < gates[2][0] - j <= n:
                    if position[gates[2][0] - j] == 0:
                        position[gates[2][0] - j] += j + 1
                        break
    else:
        # 우가 더 작음
        for i in range(gates[2][1]):
            for j in range(n):
                if 0 < gates[2][0] + j <= n:
                    if position[gates[2][0] + j] == 0:
                        position[gates[2][0] + j] += j + 1
                        break
                if 0 < gates[2][0] - j <= n:
                    if position[gates[2][0] - j] == 0:
                        position[gates[2][0] - j] += j + 1
                        break
        # 좌가 더 큼
        for i in range(gates[0][1]):
            for j in range(n):
                if 0 < gates[0][0] + j <= n:
                    if position[gates[0][0] + j] == 0:
                        position[gates[0][0] + j] += j + 1
                        break
                if 0 < gates[0][0] - j <= n:
                    if position[gates[0][0] - j] == 0:
                        position[gates[0][0] - j] += j + 1
                        break


    print(sum(position))
    print(position)
    print()