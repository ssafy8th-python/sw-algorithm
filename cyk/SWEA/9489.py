import sys
sys.stdin = open("input1.txt", "r")

T = int(input())

for tc in range(1, 1+T):
    N, M = map(int, input().split())
    build = [list(map(int, input().split())) for _ in range(N)]
    cnt_lst = []
    # 가로 판별
    for i in range(N):
        check = []
        for j in range(M):
            check.append([i, j])
        cnt = 0
        for elem in check:
            if build[elem[0]][elem[1]] == 1:
                cnt += 1
            else:
                cnt_lst.append(cnt)
                cnt = 0

        cnt_lst.append(cnt)
    # 세로 판별
    for x in range(M):
        check2 = []
        for y in range(N):
            check2.append([y, x])
        cnt1 = 0
        for elem2 in check2:
            if build[elem2[0]][elem2[1]] == 1:
                cnt1 += 1
            else:
                cnt_lst.append(cnt1)
                cnt1 = 0
        cnt_lst.append(cnt1)
    print(f'#{tc} {max(cnt_lst)}')

