def dfs(plus, minus, multiple, div, value, idx):
    global maxV, minV

    if idx == N:

        if maxV < value:
            maxV = value

        if minV > value:
            minV = value

    if plus > 0:
        dfs(plus - 1, minus, multiple, div, value + arr[idx], idx + 1)
    if minus > 0:
        dfs(plus, minus - 1, multiple, div, value - arr[idx], idx + 1)
    if multiple > 0:
        dfs(plus, minus, multiple - 1, div, value * arr[idx], idx + 1)
    if div > 0:
        if value < 0:
            value = -((value * -1) // arr[idx])
        else:
            value //= arr[idx]
        dfs(plus, minus, multiple, div - 1, value, idx + 1)


N = int(input())

arr = list(map(int, input().split()))

a, b, c, d = map(int, input().split())

maxV = -int(1e12)

minV = int(1e12)

dfs(a, b, c, d, arr[0], 1)

print(maxV)
print(minV)
