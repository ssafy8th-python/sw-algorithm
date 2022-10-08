# 1920 수 찾기
# 주소: https://www.acmicpc.net/problem/1920

# 제출한 답

# import sys
# input = sys.stdin.readline

# def binary(arr, n, key):
#     start = 0
#     end = n - 1

#     while start <= end:
#         mid = (start + end) // 2
#         if key == arr[mid]:
#             return 1
#         elif key < arr[mid]:
#             end = mid - 1
#         elif key > arr[mid]:
#             start = mid + 1
#     return 0

# N = int(input())
# N_lst = list(map(int, input().split()))
# M = int(input())
# M_lst = list(map(int, input().split()))

# N_lst.sort()

# for i in M_lst:
#     print(binary(N_lst, N, i))

# # 다른 풀이
N = int(input())
N_set = set(map(int, input().split()))
M = int(input())
M_lst = list(map(int, input().split()))

for i in M_lst:
    if i in N_set:
        print(1)
    else:
        print(0)
