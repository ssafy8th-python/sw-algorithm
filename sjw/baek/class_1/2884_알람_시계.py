# 2884 알람 시계
# 주소: https://www.acmicpc.net/problem/2884

# 제출한 답
# H, M = map(int, input().split())

# if H == 0 and M < 45:
#     H = 23
# elif M < 45 and H != 0:
#     H = H - 1

# if M < 45:
#     over_fortyfive = 45 - M
#     M = 60 - over_fortyfive
# else:
#     M = M - 45

# print(H ,M)


# 다른 답
# h, m = map(int, input().split())
# if m >= 45:
#     print(h, m-45)
# else:
#     if h == 0:
#         print(23, m+15)
#     else:
#         print(h-1, m+15)