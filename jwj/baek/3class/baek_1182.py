def subset():
    cnt = 0
    for i in range(1, 1 << N):
        target = 0
        for j in range(N):
            if i & (1 << j):
                target += arr[j]

        if target == S:
            cnt += 1

    return cnt


N, S = map(int, input().split())

arr = list(map(int, input().split()))

print(subset())
