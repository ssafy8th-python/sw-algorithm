import sys

sys.stdin = open("input_4834.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num = list(map(int, input()))

    cc = [0] * 10
    for i in num:
        cc[i] += 1

    a = 0
    maxV = 0
    for j in range(len(cc)):
        if cc[j] >= maxV:
            maxV = cc[j]
            a = j


    print(f'#{tc} {a} {maxV}')
