# 2577 숫자의 개수
# 주소: https://www.acmicpc.net/problem/2577

# 제출한 답
# sum_n = 1
# for _ in range(3):
#     num = int(input())
#     sum_n *= num
# sum_n = str(sum_n)

# result_dict = {}
# for i in range(10):
#     result_dict[i] = 0
#     for num in sum_n:
#         if int(num) == i:
#             result_dict[i] += 1
# result_lst = list(result_dict.values())
# for numv in result_lst:
#     print(int(numv))


# 다른 답
# n = str(int(input()) * int(input()) * int(input())) # 다 곱한 뒤 str로 만듦
# for i in '0123456789':                              # 0부터 9까지 차례로 반복
#     print(n.count(i))                               # count를 사용해 갯수 프린트