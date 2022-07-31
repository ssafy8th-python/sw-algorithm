# 2798 블랙잭
# 주소: https://www.acmicpc.net/problem/2798

# 제출한 답1
# N, M = map(int, input().split())
# card_lst = list(map(int, input().split()))

# max_num = 0

# for i in card_lst:
#     for j in card_lst[1:]:
#         for k in card_lst[2:]:
#             if i == j or i == k or j == k:    # 같은 걸 걸러주는 과정에서 시간이 오래걸림
#                 continue
#             result = i + j + k
#             if result >= max_num and result <= M:
#                 max_num = result

# print(max_num)



# 제출한 답2
# N, M = map(int, input().split())
# card_lst = list(map(int, input().split()))

# max_num = 0
# for i in range(N - 2):                  # 범위를 줄여줘서 더 빨라짐
#     for j in range(i + 1, N - 1):
#         for k in range(j + 1, N):
#             result = card_lst[i] + card_lst[j] + card_lst[k]
#             if result >= max_num and result <= M:
#                 max_num = result

# print(max_num)


# # 다른 답
# a,b=map(int,input().split())            # 범위를 잡아줘서 더 빠름
# c=list(map(int,input().split()))
# c.sort()
# x=c[0]+c[1]+c[2]
# for i in range(0,a-2):
#         for j in range(i+1,a-1):
#                 for k in range(j+1,a):
#                         if x<=c[i]+c[j]+c[k]<=b:
#                                 x=c[i]+c[j]+c[k]
                                
#                                 if x==b:
#                                         break
                        
# print(x)