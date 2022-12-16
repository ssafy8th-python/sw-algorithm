N, K = map(int, input().split())

arr = list(map(int, input().split()))
res = []

temp = 0

for i in range(K):
    temp += arr[i]

for i in range(1, N):
    arr[i] = arr[i] + arr[i-1]

res.append(temp)

for i in range(0, N - K):
    res.append(arr[i+K] - arr[i])

print(max(res))