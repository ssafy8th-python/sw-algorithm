# 전기버스
import sys
sys.stdin = open("input (4).txt", "r")
T = int(input())
for tc in range(1, 1+T):
    K, N, M = map(int, input().split()) # K = 3
    s = list(map(int, input().split()))
    bus_stop = [0] * (N+1)
    for i in s:
        bus_stop[i] = 1
    # print(bus_stop) # CASE 2 [0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0]
    cnt = 0 # 충전 횟수
    curIdx = K
    print(f'#{tc} ', end='')
    while True:
        if curIdx >= N: # 목적지 도달 시 끝
            print(cnt)
            break
        if curIdx < 0: # 충전 불가능
            print(0)
            break
        if bus_stop[curIdx] == 0:   #충전소가 없을 경우 1씩 되돌아감
            curIdx -= 1
        elif bus_stop[curIdx] == 1: #충전소가 있을 경우 충전소를 0으로 초기화 한 후 K만큼 이동
            bus_stop[curIdx] = 0
            curIdx += K
            cnt += 1

