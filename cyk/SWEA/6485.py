# 삼성시의 버스 노선


T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    bus_lst = [list(map(int, input().split())) for _ in range(N)]
    P = int(input())
    lstC = [int(input()) for _ in range(P)]
    bus_stop = [0] * 5001 # 버스 정류장의 수 :1번 ~ 5000번
    for i in bus_lst:
        for j in range(i[0], i[1]+1):
            bus_stop[j] += 1

    print(f'#{tc} ', end='')
    for elem in lstC:
        print(bus_stop[elem], end=' ')
    print()