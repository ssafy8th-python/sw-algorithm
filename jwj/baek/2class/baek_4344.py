C = int(input())

for _ in range(C):
    arr = list(map(int, input().split()))
    value = sum(arr[1:]) / arr[0]

    cnt = 0

    for i in arr[1:]:
        if value < i:
            cnt += 1

    result = round(cnt / arr[0], 5) * 100

    print(f'{result:.3f}%')
