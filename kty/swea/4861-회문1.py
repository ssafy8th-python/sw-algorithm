import sys

sys.stdin = open("input_4861.txt", "r")

def fel(arr):
    cnt = N-M+1
    col = list(zip(*arr))

    for i in range(cnt):
        for t in arr:
            if t[i:M+i] == t[i:M+i][::-1]:
                return t[i:M+i]

        for k in col:
            join_col = ''.join(k)
            if join_col[i:M+i] == join_col[i:M+i][::-1]:
                return join_col[i:M+i]

T = int(input())
for tc in range(1, T + 1):
    N, M = list(map(int, input().split()))
    arr = [input() for _ in range(N)]

    print(f'#{tc} {fel(arr)}')


