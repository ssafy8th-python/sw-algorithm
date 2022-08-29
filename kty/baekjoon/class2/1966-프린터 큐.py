

n = int(input())
for _ in range(n):
    num, order = map(int, input().split())
    arr = list(map(int, input().split()))
    arr_idx = list(range(num))

    cnt = 0
    while arr:
        a = arr.pop(0)
        b = arr_idx.pop(0)
        if not arr:
            cnt += 1
            print(cnt)
            break

        if a >= max(arr):
            cnt += 1
            if b == order:
                print(cnt)
                break
        else:
            arr.append(a)
            arr_idx.append(b)