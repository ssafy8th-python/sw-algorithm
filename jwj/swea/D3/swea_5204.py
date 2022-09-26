T = int(input())


def merge(left, right):
    global cnt

    if left[-1] > right[-1]:
        cnt += 1

    lp = rp = 0

    result = []

    while lp < len(left) and rp < len(right):
        if left[lp] < right[rp]:
            result.append(left[lp])
            lp += 1
        else:
            result.append(right[rp])
            rp += 1

    result.extend(left[lp:])
    result.extend(right[rp:])

    return result


def merge_sort(lst):
    if len(lst) == 1:
        return lst

    mid = len(lst) // 2

    l_list = merge_sort(lst[:mid])
    r_list = merge_sort(lst[mid:])

    return merge(l_list, r_list)


for test_case in range(1, T+1):

    N = int(input())

    lst = list(map(int, input().split()))

    cnt = 0

    result = merge_sort(lst)

    print(f'#{test_case} {result[N//2]} {cnt}')