# 11650 좌표 정렬하기
# 주소: https://www.acmicpc.net/problem/11650

# 제출한 답
# import sys
# input = sys.stdin.readline

# n = int(input())

# num_dict = {}

# for _ in range(n):
#     x, y = map(int, input().split())
#     if x in num_dict:
#         num_dict[x].append(y)
#     else:
#         num_dict[x] = [y]

# num_dict = sorted(num_dict.items())

# for i in num_dict:
#     i[1].sort()
#     for j in i[1]:
#         print(i[0], j)


# 다른 답
# import sys
# input = sys.stdin.readline
# n = int(input())

# l = []
# for _ in range(n):
#     l.append(tuple(map(int, input().split())))

# l = sorted(l)             # sort나 sorted는 인덱스 0번부터 비교하고 같다면 1번을 비교...
# for i in l:
#     print(i[0], i[1])