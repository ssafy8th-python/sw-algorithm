import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    s_arr = [list(input()) for _ in range(N)]
    for elem in s_arr:
        for i in range(N-M+1):
            a = elem[i:i+M]
            if a == a[::-1]:
                print(f'#{tc} ',end='')
                print(''.join(a))
                break

    for k in range(N):
        col_lst = []
        for x in range(N):
            col_lst.append(s_arr[x][k])
        for i in range(N - M + 1): #8
            b = col_lst[i:i+M]
            if b == b[::-1]:
                print(f'#{tc} ',end='')
                print(''.join(b))
                break
