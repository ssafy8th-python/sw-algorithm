# 8958 OX퀴즈
# 주소: https://www.acmicpc.net/problem/8958

# 제출한 답
# T = int(input())

# for _ in range(T):
#     ox = input()
#     o = 1
#     x = 0
#     result = 0

#     for idx in range(len(ox)):
#         if ox[idx] == 'X':
#             o = 1
#         elif ox[0] == 'O':
#             result += o
#             o += 1
#         elif ox[idx] != ox[idx - 1] and ox[idx] == 'O':
#             result += o
#             o += 1
#         elif ox[idx] == ox[idx - 1] and ox[idx] == 'O':
#             result += o
#             o += 1
#     print(result)


# 다른 답1
# for i in range(int(input())):
#     score = 0
#     premium = 0
#     for ox in input():                      # X면 프리미엄을 0으로 만들고 다음 반복
#         if ox == 'X':                       # O라면 프리미엄에 1을 더한 후 스코어에 더함
#             premium = 0
#             continue
#         premium += 1
#         score += premium
#     print(score)

# 다른 답2
# for i in range(int(input())):
#   score = 0
#   a = list(map(str, input().split('X')))      # X단위로 끊어서 리스트에 저장
#   for j in range(len(a)):                     # 리스트 a의 길이만큼 반복
#     if 'O' in a[j]:                           # X로 시작하는 경우를 위한 if
#       n = len(a[j])                           # n = 인덱스 j번 문자열의 길이
#       score += n*(n+1) / 2                    # 연속한 경우의 점수를 수학적으로 계산
#   print(int(score))