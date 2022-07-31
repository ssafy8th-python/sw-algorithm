# 2675 문자열 반복
# 주소: https://www.acmicpc.net/problem/2675

# 제출한 답
# T = int(input())
# for _ in range(T):
#     R, S = input().split()
#     R = int(R)

#     result = ''
#     for word in S:
#         result += word * R
#     print(result)


# 다른 답
# T = int(input())
# for i in range(T):
#   N,S = map(str,input().split())
#   N = int(N)                       # 제출한 답과 동일

#   for i in range(len(S)):
#     print(S[i]*N,end="")           # end=''을 사용해 옆으로 프린트함
#   print()