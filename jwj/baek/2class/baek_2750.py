def merge(left, right):
    lp = rp = 0

    res = []

    while lp < len(left) and rp < len(right):
        if left[lp] < right[rp]:
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

    l_list = merge_sort(lst[:mid])
    r_list = merge_sort(lst[mid:])

    return merge(l_list, r_list)


N = int(input())

arr = []

for _ in range(N):
    num = int(input())
    arr.append(num)

result = merge_sort(arr)

for r in result:
    print(r)
