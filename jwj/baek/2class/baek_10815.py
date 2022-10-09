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

    l_lst = merge_sort(lst[:mid])
    r_lst = merge_sort(lst[mid:])

    return merge(l_lst, r_lst)


def binary_search(num):
    start = 0
    end = N - 1

    while start <= end:
        mid = (start + end) // 2

        if result1[mid] == num:
            return 1

        if result1[mid] < num:
            start = mid + 1

        else:
            end = mid - 1

    return 0


N = int(input())

arr1 = list(map(int, input().split()))

result1 = merge_sort(arr1)

M = int(input())

arr2 = list(map(int, input().split()))

for n in arr2:
    print(binary_search(n), end=' ')
print()
