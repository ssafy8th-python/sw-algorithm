# 10814 나이순 정렬
# 주소: https://www.acmicpc.net/problem/10814

# 제출한 답         import안하면 완전 느리게 나옴
# import sys
# input = sys.stdin.readline

# n = int(input())

# data = {}

# for _ in range(n):
#     x, y = input().split()
#     x = int(x)
#     if x in data:
#         data[x].append(y)
#     else:
#         data[x] = [y]

# data = sorted(data.items(), key= lambda x : int(x[0]))

# for i in data:
#     for j in i[1]:
#         print(i[0], j)


# 다른 답
# import sys
# input = sys.stdin.readline          # 빠른 입력을 위한 것
# [print(i[0], i[1])                  # 튜플을 차례로 출력

# for i in                            # 정렬된 리스트 내의 값들을 차례로 반복

# sorted([tuple(input().split())      # 리스트 컴프리헨션 사용해서 입력값마다 리스트에 튜플로 저장

# for _ in range(int(input()))],      # n만큼 반복

#  key = lambda x : int(x[0]))]       # 각 튜플의 인덱스 0번 기준으로 정렬

# 실제 코드: [print(i[0], i[1]) for i in sorted([tuple(input().split()) for _ in range(int(input()))], key=lambda x:int(x[0]))]
