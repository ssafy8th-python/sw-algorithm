import sys

sys.stdin = open("input_1859.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    stuff = list(map(int, input().split()))

    cost = 0
    maxV = 0
    for i in range(N-1, -1, -1): # 뒤에서 부터 봄
        if stuff[i] > maxV:
            maxV = stuff[i]
        else:
            cost += maxV - stuff[i]

    print(f'#{tc} {cost}')