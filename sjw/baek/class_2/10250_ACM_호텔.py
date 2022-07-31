# 10250 ACM 호텔
# 주소: https://www.acmicpc.net/problem/10250

# 제출한 답
# T = int(input())

# for _ in range(T):
#     room = ''
#     H, W, N = map(int,input().split())

#     ho = (N // H) + 1
#     floor = N % H

#     if floor == 0:
#         if ho - 1 < 10:
#             room += str(H) + '0' + str(ho - 1)
#         else:
#             room += str(H) + str(ho - 1)

#     elif ho < 10:
#         room += str(floor) + '0' + str(ho)
#     else:
#         room += str(floor) + str(ho)
    
#     print(int(room))

# 다른 답
# T = int(input())

# for t in range(T):
#     H, W, N = map(int,input().split())  # 제출한 답과 큰 틀에서는 같음
#     floor = (((N - 1) % H) + 1) * 100   # floor: N-1을 안하면 1 2 3 4 5 0 이지만 
#     ho = (N - 1) // H + 1               # N-1을 하면 0 1 2 3 4 5 임  - H = 6 기준
#     room = floor + ho                   # ho: N-1을 안하면 0 0 1 1 1 2 2 2 3 이지만
#                                         # N-1을 하면 0 0 0 1 1 1 2 2 2 이됨  - 3 X 3 기준
#     print(room)