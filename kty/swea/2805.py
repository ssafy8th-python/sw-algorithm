import sys

sys.stdin = open("input_2805.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]

    mid = n // 2
    st = ed = mid
    sumV = 0

    for row in range(n):
        for col in range(st, ed + 1):
            sumV += arr[row][col]

        if row < mid:
            st -= 1
            ed += 1

        else:
            st += 1
            ed -= 1

    print(f'#{tc} {sumV}')