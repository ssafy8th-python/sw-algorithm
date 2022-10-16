N = int(input())

arr = list(map(int, input().split()))

left = 0
right = N - 1
minV = 2000000000

result = [0, 0]
while left < right:
    n_v = arr[left] + arr[right]

    if abs(n_v) < minV:
        minV = abs(n_v)
        result[0] = arr[left]
        result[1] = arr[right]

    if n_v == 0:
        break

    if n_v < 0:
        left += 1
    elif n_v > 0:
        right -= 1

print(*result)