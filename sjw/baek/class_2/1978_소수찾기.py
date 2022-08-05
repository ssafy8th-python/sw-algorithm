# 1978 소수 찾기
# 주소: https://www.acmicpc.net/problem/1978

# 제출한 답
# n = int(input())

# num_lst = list(map(int, input().split()))
# sosu = 0
# for i in num_lst:
#     m = 2
#     k = 0
#     while m <= i:
#         if i % m == 0:
#             k += 1
#         m += 1
#     if k == 1:
#         sosu += 1
# print(sosu)

# 다른 답
# n = int(input())

# nums = list(map(int, input().split()))
# cnt = n

# for elem in nums:
#     if elem > 2:
#         for i in range(2, elem-1):
#             if elem % i == 0:   #소수가 아니면
#                 cnt -= 1        #전체에서 빼준다
#                 break
#     elif elem == 1:
#         cnt -= 1
# print(cnt)