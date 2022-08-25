import sys

sys.stdin = open("input_5097.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    for _ in range(m):
        arr.append(arr.pop(0))

    print(f'#{tc } {arr[0]}')