import sys
input = sys.stdin.readline

N = int(input())

students = [[] for _ in range(N * N + 1)]

school = [[0] * N for _ in range(N)]

for _ in range(N*N):
    student = list(map(int, input().split()))
    students[student[0]].extend(student[1:])

    # 자리배치

    # 1번 좋아하는 학생이 인접한 칸이 가장 많을 때
    like_lst = [[0] * N for _ in range(N)]
    empty_lst = [[0] * N for _ in range(N)]
    seat_x = -1
    seat_y = -1

    for i in range(N):
        for j in range(N):
            # 이미 학생이 앉아 있는 경우
            if school[i][j]:
                continue

            if seat_x == -1:
                seat_x = i
                seat_y = j

            # 좋아하는 학생
            like = 0
            # 비어있는 칸
            empty = 0
            for d_x, d_y in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                n_x = i + d_x
                n_y = j + d_y
                if 0 <= n_x < N and 0 <= n_y < N:
                    if school[n_x][n_y] in students[student[0]]:
                        like += 1
                    elif school[n_x][n_y] == 0:
                        empty += 1

            like_lst[i][j] = like
            empty_lst[i][j] = empty

    max_like = 0
    max_empty = 0
    # 행의 번호가 가장 적은, 열의 번호가 가장 적은
    for i in range(N):
        for j in range(N):
            if school[i][j]:
                continue
            if max_like < like_lst[i][j]:
                max_like = like_lst[i][j]
                seat_x = i
                seat_y = j
                max_empty = empty_lst[i][j]
            elif max_like == like_lst[i][j]:
                if max_empty < empty_lst[i][j]:
                    seat_x = i
                    seat_y = j
                    max_empty = empty_lst[i][j]

    school[seat_x][seat_y] = student[0]

result = 0

for i in range(N):
    for j in range(N):
        cnt = 0
        for d_x, d_y in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            n_x = i + d_x
            n_y = j + d_y
            if 0 <= n_x <N and 0 <= n_y < N:
                if school[n_x][n_y] in students[school[i][j]]:
                    cnt += 1

        if cnt == 1:
            result += 1
        elif cnt == 2:
            result += 10
        elif cnt == 3:
            result += 100
        elif cnt == 4:
            result += 1000

print(result)