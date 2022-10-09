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


N, M = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

result = merge(A, B)

print(*result)