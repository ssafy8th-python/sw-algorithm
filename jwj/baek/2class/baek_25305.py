
def merge(left, right):
    lp = rp = 0

    res = []

    while lp < len(left) and rp < len(right):
        if left[lp] > right[rp]:
            res.append(left[lp])
            lp += 1
        else:
            res.append(right[rp])
            rp += 1

    res.extend(left[lp:])
    res.extend(right[rp:])

    return res


def merge_sort(lst):
    if len(lst) == 1:
        return lst

    mid = len(lst) // 2

    l_lst = merge_sort(lst[:mid])
    r_lst = merge_sort(lst[mid:])

    return merge(l_lst, r_lst)


N, k = map(int, input().split())

arr = list(map(int, input().split()))

result = merge_sort(arr)

print(result[k-1])