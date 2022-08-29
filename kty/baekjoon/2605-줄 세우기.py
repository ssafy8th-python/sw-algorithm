n = int(input())
arr = list(map(int, input().split()))
result = []
for i in range(len(arr)):
    result.insert(i-arr[i], i+1)

print(*result)