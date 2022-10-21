import sys
input = sys.stdin.readline

N = int(input())

board = list(input().split())

dp = [[0] * N for _ in range(N)]

for num_len in range(N):
    for start in range(N-num_len):
        end = start + num_len
        if start == end:
            dp[start][end] = 1

        elif board[start] == board[end]:
            if start + 1 == end:
                dp[start][end] = 1
            elif dp[start+1][end-1] == 1:
                dp[start][end] = 1


M = int(input())


for _ in range(M):
    S, E = map(int, input().split())

    print(dp[S-1][E-1])