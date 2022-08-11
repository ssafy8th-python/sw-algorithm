T = int(input())

for tc in range(1, T+1):
    n, k = map(int, input().split())
    arr_A = list(range(1, 13))

    len_arrA = len(arr_A)
    result = []

    for i in range(1 << len_arrA):
        lst = []
        s = 0
        for j in range(len_arrA):
            if i & (1 << j):
                lst.append(arr_A[j])
        for j in lst:
            s += j
        if len(lst) == n and s == k:
            result.append(lst)
    print(f'#{tc} {len(result)}')