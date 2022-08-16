import sys

sys.stdin = open("input_3143.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    str1, str2 = input().split()

    cnt = 0
    while len(str1) != 0:
        if str1.startswith(str2):
            cnt += 1
            str1 = str1[len(str2):]
        else:
            cnt += 1
            str1 = str1[1:]

    print(f'#{tc} {cnt}')