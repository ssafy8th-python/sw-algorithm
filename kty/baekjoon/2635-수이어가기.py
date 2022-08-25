n = int(input())

maxV = 0
result = []
for i in range(1, n+1):
    first = n
    second = i
    arr = [first, second]
    while True:
        next = first - second
        if next >= 0:
            arr.append(next)
            first, second = second, next
        else:
            if len(arr) > maxV:
                maxV = len(arr)
                result = arr
            break

print(maxV)
print(*result)

