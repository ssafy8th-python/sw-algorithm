import sys

sys.stdin = open("input_1289.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    num = input()
    k = '0'
    cnt = 0
    for i in num:
        if k != i:
            cnt += 1
            k = i

    print(f'#{tc} {cnt}')
