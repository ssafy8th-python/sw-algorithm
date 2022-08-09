import sys

sys.stdin = open("input_4831.txt", "r")

T = int(input())
for tc in range(1, T+1):
    K, N, M = list(map(int, input().split()))
    charge_station = list(map(int, input().split()))

    here = 0
    charge = 0
    while here + K < N:
        for i in range(K, 0, -1):
            if here + i in charge_station:
                here += i
                charge += 1
                break

        else:
            charge = 0
            break

    print(f'#{tc} {charge}')




