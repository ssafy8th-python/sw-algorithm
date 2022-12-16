def merge(left, right):
    global cnt, answer

    lp = rp = 0

    result = []

    while lp < len(left) and rp < len(right):
        if left[lp] > right[rp]:
            result.append(right[rp])
            rp += 1
            cnt += 1
            if cnt == K:
                answer = result[-1]
        else:
            result.append(left[lp])
            cnt += 1
            lp += 1
            if cnt == K:
                answer = result[-1]

    while lp < len(left):
        result.append(left[lp])
        lp += 1
        cnt += 1
        if cnt == K:
            answer = result[-1]

    while rp < len(right):
        result.append(right[rp])
        rp += 1
        cnt += 1
        if cnt == K:
            answer = result[-1]

    return result


def merge_sort(lst):
    if len(lst) == 1:
        return lst

    mid = (len(lst)+1) // 2

    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])

    return merge(left, right)


A, K = map(int, input().split())

lst = list(map(int, input().split()))

cnt = 0

answer = -1

merge_sort(lst)

print(answer)