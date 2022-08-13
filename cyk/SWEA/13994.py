# 새로운 버스 노선
import sys
sys.stdin = open("sample_in.txt", "r")

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    station = [0] * 1001
    cnt = 0

    for _ in range(n):
        bus_type, A, B = map(int, input().split())
        station[A] += 1
        station[B] += 1

        if bus_type == 1:
            for i in range(A+1,B):
                station[i] += 1
        if bus_type == 2:
            if A % 2: # 홀수 ->  홀수 번호
                for i in range(A+2, B, 2):
                    station[i] += 1
            else: # 짝수 -> 짝수 번호
                for i in range(A+2, B, 2):
                    station[i] += 1


        if bus_type == 3:
            if A % 2: #홀수 ->3의 배수이면서 10의 배수가 아닌 번호 정류장에 정차
                for i in range(A+1, B):
                    if i % 3 == 0 and i % 10 != 0:
                        station[i] += 1

            else: #짝수 4의 배수 번호 정류장
                for i in range(A+1, B):
                    if i % 4 == 0:
                        station[i] += 1

    print(f'#{tc} {max(station)}')
