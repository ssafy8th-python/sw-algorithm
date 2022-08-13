import sys

sys.stdin = open("input_13994.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    road = [0] * 1001
    for i in range(N):
        bus, st, ed = list(map(int, input().split()))
        road[st] += 1
        road[ed] += 1

        if bus == 1: # 일반
            for j in range(st+1, ed):
                road[j] += 1
        elif bus == 2: # 급행
            if st % 2: # 급행 홀수 일때
                for j in range(st+1, ed):
                    if j % 2:
                        road[j] += 1
            else: # 급행 짝수 일때
                for j in range(st+1, ed):
                    if j % 2 == 0:
                        road[j] += 1
        else: # 광역 급행
            if st % 2: # 광역 급행 버스 홀수 일때
                for j in range(st+1, ed):
                    if j % 3 == 0 and j % 10 != 0: # 3의 배수이면서 10의 배수가 아닐 때
                        road[j] += 1
            else: # 광역 급행 버스 짝수 일 때
                for j in range(st+1, ed):
                    if j % 4 == 0: # 4의 배수 일때
                        road[j] += 1

    maxV = 0
    for k in road:
        if k > maxV:
            maxV = k
    print(f'#{tc} {maxV}')
