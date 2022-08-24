K, N = map(int, input().split())


def search(start, end):
    global result

    while start <= end:
        total = 0

        mid = (start + end) // 2

        for i in range(K):
            total += lanseon[i] // mid

        if total < N:
            end = mid - 1
        else:
            start = mid + 1
            result = mid


lanseon = []
for i in range(K):
    lanseon.append(int(input()))


start = 1
end = max(lanseon)
result = 0

search(start, end)

print(result)
