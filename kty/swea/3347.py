import sys

sys.stdin = open("input_3347.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    n, m = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    vote = [0] * n
    for i in range(m):
        for j in range(n):
            if b[i] >= a[j]:
                vote[j] += 1
                break

    maxV = 0
    max_idx = 0
    for i in range(len(vote)):
        if vote[i] > maxV:
            maxV = vote[i]
            max_idx = i

    print(f'#{tc} {max_idx+1}')