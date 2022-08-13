T = int(input())

for tc in range(1, T+1):
    N = int(input())

    station_lst = [0] * 1001

    for _ in range(N):
        bus, A, B = map(int, input().split())

        station_lst[A] += 1
        station_lst[B] += 1

        if bus == 1:
            for station in range(A+1, B):
                station_lst[station] += 1

        elif bus == 2:
            for station in range(A+1, B):
                if A % 2 == 0 and station % 2 == 0:
                    station_lst[station] += 1
                elif A % 2 == 1 and station % 2 == 1:
                    station_lst[station] += 1

        elif bus == 3:
            if A % 2:
                for station in range(A+1, B):
                    if station % 10 and station % 3 == 0:
                        station_lst[station] += 1
            else:
                for station in range(A+1, B):
                    if station % 4 == 0:
                        station_lst[station] += 1

    maxV = station_lst[0]

    for num in station_lst:
        if maxV < num:
            maxV = num

    print(f'#{tc} {maxV}')
