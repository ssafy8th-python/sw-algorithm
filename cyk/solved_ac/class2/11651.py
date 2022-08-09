N = int(input())

# lst = [list(map(int,input().split())) for _ in range(N)]

# sorted_lst = sorted(lst, key=lambda x :x[1])

# for num in range(N-1):
#     if sorted_lst[num][1] == sorted_lst[num+1][1]:
#         if sorted_lst[num][0] > sorted_lst[num][1] :
#             sorted_lst[num], sorted_lst[num+1] = sorted_lst[num+1], sorted_lst[num]

# for elem in sorted_lst :
#     print(elem[0], elem[1])

# FAIL

lst = []

for _ in range(N) :
    x, y = map(int, input().split())
    lst.append([y,x])

for elem in sorted(lst) :
    print(elem[1], elem[0])