# import sys
#
# sys.stdin = open("input_4408.txt", "r")
#
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     room_list = [list(map(int, input().split())) for _ in range(N)]
#
#     bokdo = [0] * 201
#     for room in room_list:
#         if room[0] < room[1]:
#             for i in range(room[0] // 2, room[1] // 2 + 1):
#                 bokdo[i] += 1
#         else:
#             for j in range(room[1] // 2, room[0] // 2 + 1):
#                 bokdo[j] += 1
#
#     time = 0
#     for t in range(len(bokdo)):
#         if bokdo[t] > time:
#             time = bokdo[t]
#     print(f'#{tc} {time}')

import sys

sys.stdin = open("input_4408.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    room_list = [list(map(int, input().split())) for _ in range(N)]

    bokdo = [0] * 201
    for room in room_list:
        if room[0] > room[1]:
            room[0], room[1] = room[1], room[0]
        for i in range((room[0]+1)//2, (room[1]+1)//2 + 1):
            bokdo[i] += 1

    time = 0
    for t in bokdo:
        if t > time:
            time = t
    print(f'#{tc} {time}')