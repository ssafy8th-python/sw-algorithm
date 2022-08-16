import sys

sys.stdin = open("input_5356.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    arr = [input() for _ in range(5)]
    new_arr = [[False] * 15 for _ in range(5)]
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            new_arr[i][j] = arr[i][j]

    words = ''
    for k in range(15):
        for t in range(5):
            if new_arr[t][k] != False:
                words += new_arr[t][k]

    print(f'#{tc} {words}')