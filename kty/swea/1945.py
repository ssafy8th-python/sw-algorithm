import sys

sys.stdin = open("input_1945.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    num = int(input())
    soin = [2, 3, 5, 7 ,11]
    soin_lst = [0] * 5
    for i in range(len(soin)):
        while num % soin[i] == 0:
            num //= soin[i]
            soin_lst[i] += 1

    print(f'#{tc}', end=' ')
    print(*soin_lst)

