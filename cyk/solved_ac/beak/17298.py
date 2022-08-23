# 오큰수
N = int(input())
s = list(map(int, input().split())) # [3, 5, 7, 2]
result = []
temp = []

for i in range(len(s)-1, -1, -1):
    if not temp:
        result.append(-1)
        temp.append(s[i])
    else:
        if temp[-1] > s[i]:
            result.append(temp[-1])
            temp.append(s[i])
        else:
            while temp and temp[-1] <= s[i]:
                temp.pop()
            if not temp:    # temp가 비었을 때
                result.append(-1)
                temp.append(s[i])

            else:
                result.append(temp[-1])
                temp.append(s[i])


print(*result[::-1])









# ST = [-1, s[-1]]   # -1을 미리 넣어줌
# i = 1
# s == s[::-1]
# checkST = [s[-1]]
# while i < len(s):    # s에 요소가 있을 때까지
#     if s[i] < checkST[-1]:
#         ST.append(checkST[-1])
#         checkST.append(s[i])
#
#     else:
#         while s[i] > checkST[-1]:
#             checkST.pop()
#         checkST.append(s[i])
#     i += 1
# print(ST[::-1])

