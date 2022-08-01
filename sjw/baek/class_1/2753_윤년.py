# 2753 윤년
# 주소: https://www.acmicpc.net/problem/2753

# 제출한 답
# year = int(input())

# if year % 4 == 0 and year % 100 != 0:
#     print(1)
# elif year % 400 == 0:
#     print(1)
# else:
#     print(0)


# 다른 답
# a = int(input())
# print(int(a % 4 == 0 and (a % 100 != 0 or a % 400 == 0)))
# a를 4로 나눈 나머지가 0이고(and) a를 100으로 나눈 나머지가 0이 아닌 경우거나
# a를 4로 나눈 나머지가 0이고(and) a를 400으로 나눈 나머지가 0인 경우
# True가 나오고 이걸 int로 정수로 바꿔주면 1로 나옴
# False인 경우 int로 정수로 바꿔주면 0이 나옴