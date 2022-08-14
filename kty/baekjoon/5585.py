N = int(input())
arr = [500, 100, 50, 10, 5, 1]
cnt = 0
cost = 1000 - N
for i in range(len(arr)):
    cnt += cost // arr[i]
    cost = cost % arr[i]

print(cnt)