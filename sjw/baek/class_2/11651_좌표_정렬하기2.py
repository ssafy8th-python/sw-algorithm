# 11651 좌표 정렬하기2
# 주소: https://www.acmicpc.net/problem/11651

# 제출한 답
# import sys
# input = sys.stdin.readline

# n = int(input())

# num_dict = {}

# for _ in range(n):
#     x, y = map(int, input().split())
#     if y in num_dict:
#         num_dict[y].append(x)
#     else:
#         num_dict[y] = [x]

# num_dict = sorted(num_dict.items())

# for i in num_dict:
#     i[1].sort()
#     for j in i[1]:
#         print(j, i[0])


# 다른 답
# import sys
# read = sys.stdin.readline

# nums = [list(map(int, read().split())) for _ in range(int(read()))]  # 리스트 컴프리헨션으로 리스트 생성

# for x, y in sorted(nums, key=lambda x: (x[1], x[0])):                # (y, x)로 정렬
#     print(x, y)                                                      # 정렬된 것을 x, y로 출력