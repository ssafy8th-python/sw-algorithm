# 2231 분해합
# 주소: https://www.acmicpc.net/problem/2231

# 제출한 답
# def ger(num):
#     for i in range(num):
#         M = 0
#         M += i
#         i = str(i)
#         for j in i:
#             M += int(j)
#         if M == num:
#             return print(int(i))
#     return print(0)
        
# ger(int(input()))


# 다른 답
# import sys
# input = sys.stdin.readline               # input시간마저 줄이려는 노력

# N = int(input())
# ans = 0                         # 생성자가 없을 떄 기본적으로 출력될 0
# s = N - 9 * len(str(N))         # range 범위 줄이기 위함
# for i in range(s, N):           #  각 자리수에서 가장 큰 수는 9이고 어차피 더해서 N이 나와야하기 때문임
#     n = i + sum(map(int, list(str(i)))) # 리스트를 sum함수를 통해 더함
#     if n == N:                          # n과 N이 같으면 ans = i가 됨
#         ans = i
#         break

# print(ans)