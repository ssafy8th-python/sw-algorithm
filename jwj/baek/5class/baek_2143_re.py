def two_pointer(lst):

    n_len = len(lst)

    result = []

    for i in range(n_len):
        rp = i + 1
        sum_value = lst[i]
        result.append(sum_value)

        for j in range(n_len - i - 1):
            sum_value += lst[rp]
            result.append(sum_value)
            rp += 1

    return result


def binary_search_left(lst, target):
    result = 1

    start = 0
    end = len(lst) - 1

    while start <= end:
        mid = (start + end) // 2

        if lst[mid] > target:
            end = mid - 1
        elif lst[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
            result = mid

    return result


def binary_search_right(lst, target):

    result = 0

    start = 0
    end = len(lst) - 1

    while start <= end:
        mid = (start + end) // 2

        if lst[mid] > target:
            end = mid - 1
        elif lst[mid] < target:
            start = mid + 1
        else:
            start = mid + 1
            result = mid

    return result

T = int(input())

n = int(input())

A = list(map(int, input().split()))

m = int(input())

B = list(map(int, input().split()))

result = 0

A_lst = two_pointer(A)
B_lst = two_pointer(B)
A_lst.sort()
B_lst.sort()

for i in A_lst:
    l = binary_search_left(B_lst, T - i)
    r = binary_search_right(B_lst, T - i)

    result += r - l + 1

print(result)
