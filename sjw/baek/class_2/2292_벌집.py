# 2292 벌집
# 주소: https://www.acmicpc.net/problem/2292

# 제출한 답
# N = int(input())
# count = 1
# mini = 1
# maxi = 0
# maxi_sub = 1
# while True:
#     if N == 1:
#         print(1)
#         break
#     elif N >= 2 * mini and N <= 6 * (maxi + maxi_sub) + 1:
#         print(count + 1)
#         break
#     else:
#         mini += 3
#         maxi += maxi_sub
#         maxi_sub += 1
#         count += 1


# 다른 답1
# n = int(input())    # 숫자입력

# cnt = 1             # 카운트(기본 1)              단계별 시작구간이
#                     #                            구구단 6단 단위로 증가하므로
# while n>1:          # n이 1보다 클 동안           이런 풀이가 가능
#     n -= (6*cnt)    # n에서 6 X 카운트 만큼 빼기
#     cnt +=1         # 카운트 + 1

# print(cnt)          # 카운트 프린트


# 다른 답2
# n = int(input())            # 다른 답1과 달리 쌓아가는 방식

# nums_pileup = 1  
# cnt = 1
# while n > nums_pileup :
#     nums_pileup += 6 * cnt  
#     cnt += 1  
# print(cnt)