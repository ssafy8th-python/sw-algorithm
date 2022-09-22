# 최대상금
# 최대 여섯자리수, 최대 10번의 교환횟수
'''
1
123 1
'''
# def f(k, lst):
#     global res
#     if k == count:
#         tmp = ''
#         for elem in lst:
#             tmp += f'{elem}'
#             if res < int(tmp):
#                 res = int(tmp)
#         return
#     if lst in arrList[k]:
#         return
#     else:
#         arrList[k].append(lst)
#
#     for i in range(size):
#         for j in range(i+1, size):
#             lst[i], lst[j] = lst[j], lst[i]
#
#             f(k+1, lst)
#             lst[i], lst[j] = lst[j], lst[i]
#
#
# T = int(input())
# for tc in range(1, 1+T):
#     num_lst, count = input().split()
#     num_lst, count= list(num_lst), int(count)
#     size = len(num_lst)
#     res = 0
#     arrList = [[] for _ in range(count)]
#     f(0, num_lst)
#     print(f'#{tc} {res}')

# def perm(lst, depth, n, k,cnt):
#     global res
#     if cnt == n:
#         tmp = ""
#         for elem in lst:
#             tmp += elem
#         if res < int(tmp):
#             res = int(tmp)
#         return
#
#     if cnt == k:
#         tmp = ""
#         for elem in lst:
#             tmp += elem
#         if res < int(tmp):
#             res = int(tmp)
#         return
#     if depth >= n:
#         return
#
#     for i in range(n):
#         lst[i], lst[depth] = lst[depth], lst[i]
#         if i == depth:
#             perm(lst, depth+1, n, k, cnt)
#         else:
#             perm(lst, depth+1, n, k, cnt+1)
#         lst[i], lst[depth] = lst[depth], lst[i]
#
#
#
# T = int(input())
# for tc in range(1, 1+T):
#     num_lst, count = input().split()
#     num_lst, count= list(num_lst), int(count)
#     size = len(num_lst)
#     res = 0
#     perm(num_lst,0,len(num_lst), count, 0)
#     if count > size:
#         tmp = ''
#         if (count - size)%2:
#             for i in range(size-2):
#                 tmp += str(res)[i]
#             tmp += str(res)[-1]
#             tmp += str(res)[-2]
#             res = tmp
#     print(f'#{tc} {res}')


def f(k, lst):
    global res
    if k == count:
        tmp = ''
        for elem in lst:
            tmp += f'{elem}'
            if res < int(tmp):
                res = int(tmp)
        return

    if lst in arrList[k]:
        return
    else:
        arrList[k].append(lst)


    for i in range(size):
        for j in range(i + 1, size):
            new_lst = lst[::]
            x = lst[i]
            y = lst[j]
            new_lst[i], new_lst[j] = y, x
            f(k + 1, new_lst)


T = int(input())
for tc in range(1, 1 + T):
    num_lst, count = input().split()
    num_lst, count = list(map(int, list(num_lst))), int(count)
    size = len(num_lst)
    res = 0
    arrList = [[] for _ in range(count)]

    f(0, num_lst)
    print(f'#{tc} {res}')