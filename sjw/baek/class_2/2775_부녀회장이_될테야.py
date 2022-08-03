# 2775 부녀회장이 될테야
# 주소: https://www.acmicpc.net/problem/2775

# 제출한 답
# 층 수만큼 리스트를 만들어서 다른 리스트에 넣음
# k층의 n호 프린트

# T = int(input())

# init_lst = list(range(1, 15)) # 0층

# for _ in range(T):
#     k = int(input())    # 층
#     n = int(input())    # 호

#     apart = [init_lst]  # 아파트 2차원 리스트
#     for i in range(k):  # 층 수 만큼 반복
#         floor = [1]     # 각 층을 넣을 리스트
#         for j in range(1, 14):
#             new_room = floor[j - 1] + apart[i][j]
#             floor.append(new_room)  # 바로 전 호수 + 아래층 j번 호수
#         apart.append(floor)

#     print(apart[k][n-1])  # 아파트 k층의 n-1번 인덱스호


# 다른 답
# t = int(input())

# for _ in range(t):  
#     floor = int(input())  # 층
#     num = int(input())  # 호
#     f0 = [x for x in range(1, num+1)]  # 0층 리스트
#     for k in range(floor):  # 층 수 만큼 반복
#         for i in range(1, num):  # 1 ~ n-1까지 (인덱스로 사용)
#             f0[i] += f0[i-1]  # 층별 각 호실의 사람 수를 변경
#     print(f0[-1])  # 가장 마지막 수 출력