'''
1 ≤ N ≤ 100,000

입력
5
4 1 5 2 3

5
1 3 7 9 5

출력
1
1
0
0
1
'''



# 오답 - 시간초과
# import sys
# input = sys.stdin.readline
#
# N = int(input())
# A_lst = list(map(int, input().split()))
#
# M = int(input())
# M_lst = list(map(int, input().split()))
#
# x  = list(set(A_lst)&set(M_lst)) [1, 3, 5]
#
# for elem in M_lst :
#     if x.count(elem) == 0 :
#         print(0)
#     else :
#         print(1)

import sys

input = sys.stdin.readline

N = int(input())
a = (map(int, input().split()))

dict_a = {x : 1 for x in a} # {4:1, 1:1, 5:1, 2:1, 3:1}

M = int(input())
m = (map(int, input().split()))


for k in m :
    if dict_a.get(k) == 1 :
        print(1)
    else :
        print(0)



