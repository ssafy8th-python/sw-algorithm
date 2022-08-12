import sys

sys.stdin = open("input_9386.txt", "r")


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num = list(map(int, input()))

    maxV = 0
    cnt = 0
    for i in range(N):
        if num[i] == 1:
            cnt += 1
            if maxV < cnt:
                maxV = cnt
        else:
            cnt = 0

    print(f'#{tc} {maxV}')
