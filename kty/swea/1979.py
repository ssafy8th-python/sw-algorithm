import sys

sys.stdin = open("input_1979.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N, K = list(map(int, input().split()))
    puzzle = [list(map(int, input().split())) for _ in range(N)]

##

    cnt = 0
    for i in range(N):
        track = 1
        track_r_cnt = 0
        track_c_cnt = 0
        for j in range(N):
            if puzzle[i][j] == track:
                track_r_cnt += 1
                if j == N-1:
                    if track_r_cnt == K:
                        cnt += 1
                        track_r_cnt = 0
            else:
                if j == N:
                    if track_r_cnt == K:
                        cnt += 1
                if track_r_cnt == K:
                    cnt += 1
                track_r_cnt = 0

            if puzzle[j][i] == track:
                track_c_cnt += 1
                if i == N:
                    if track_c_cnt == K:
                        cnt += 1
                        track_c_cnt = 0
            else:
                if j == N-1:
                    if track_c_cnt == K:
                        cnt += 1
                if track_c_cnt == K:
                    cnt += 1
                track_r_cnt = 0
    print(f'#{tc} {cnt)
