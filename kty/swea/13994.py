import sys

sys.stdin = open("input_13994.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    bus = [list(map(int, input().split())) for _ in range(N)]
    road = [0] * 1000
    for i in range(N):
        if bus[i][0] == 1: # 일반
            for j in range(bus[i][1], bus[i][2]+1):
                road[j] += 1
        elif bus[i][0] == 2: # 급행
            if bus[i][1] % 2: # 급행 홀수 일때
                for j in range(bus[i][1], bus[i][2] + 1):
                    if j % 2: # 홀수 번째 정류장에 카운트
                        road[j] += 1
                if bus[i][2] % 2 == 0: # 급행 홀수 버스의 마지막 정류장 번호가 짝수이면 카운트가 안되니깐 따로 카운트 추가
                    road[bus[i][2]] += 1
            else: # 급행 짝 수 일때
                for j in range(bus[i][1], bus[i][2] + 1):
                    if j % 2 == 0: # 짝수 번째 정류장에 카운트
                        road[j] == 1
                if bus[i][2] % 2: # 급행 짝수 버스의 마지막 정류장 번호가 홀수이면 카운트가 안되니깐 따로 카운트 추가
                    road[bus[i][2]] += 1
        else: # 광역 급행
            if bus[i][1] % 2: # 광역 급행 버스 홀수 일때
                for j in range(bus[i][1], bus[i][2] + 1):
                    if j % 3 == 0 and j % 10 != 0: # 3의 배수이면서 10의 배수가 아닐 때
                        road[j] += 1
                if bus[i][1] % 3 != 0 or bus[i][1] % 10 == 0: # 시작 정류장이 3의 배수가 아니거나 10의 배수일 때 따로 카운트를 해줌.
                    road[bus[i][1]] += 1
                if bus[i][2] % 3 != 0 or bus[i][2] % 10 == 0:  # 끝 정류장이 3의 배수가 아니거나 10의 배수일 때 따로 카운트를 해줌.
                    road[bus[i][2]] += 1
            else: # 광역 급행 버스 짝수 일 때
                for j in range(bus[i][1], bus[i][2] + 1):
                    if j % 4 == 0: # 4의 배수 일때
                        road[j] += 1
                if bus[i][1] % 4 != 0: # 시작 정류장이 4의 배수가 아닐때 따로 카운트를 해줌.
                    road[bus[i][1]] += 1
                if bus[i][2] % 4 != 0: # 끝 정류장이 4의 배수가 아닐때 따로 카운트를 해줌.
                    road[bus[i][2]] += 1

    maxV = 0
    for k in road:
        if k > maxV:
            maxV = k
    print(f'#{tc} {maxV}')
    print(road)






