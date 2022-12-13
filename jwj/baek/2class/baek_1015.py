n = int(input())

P = list(map(int, input().split()))

arr = [0] * 1001

for num in P:
    arr[num] += 1

res = [0] * 1001


for i in range(1, 1001):
    arr[i] = arr[i-1] + arr[i]

for num in P:
    print(arr[num-1] + res[num], end=" ")
    res[num] += 1

