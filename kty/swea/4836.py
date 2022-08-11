import sys

sys.stdin = open("input_4836.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num = [list(map(int, input().split())) for _ in range(N)]

    red = []
    blue = []
    for i in range(len(num)):
        if num[i][-1] == 1: # 빨강 이면
            for x in range(num[i][2] - num[i][0] + 1):
                for y in range(num[i][3] - num[i][1] + 1):
                    red.append([num[i][0] + x, num[i][1] + y])

        elif num[i][-1] == 2: # 파랑 이면
            for x in range(num[i][2] - num[i][0] + 1):
                for y in range(num[i][3] - num[i][1] + 1):
                    blue.append([num[i][0] + x, num[i][1] + y])

    violet = []
    for same in red:
        if same in blue:
            violet.append(same)

    print(f'#{tc} {len(violet)}')