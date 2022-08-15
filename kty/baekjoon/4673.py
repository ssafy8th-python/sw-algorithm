n = 10000
arr = [True] * 100000

for i in range(1, n+1):
    sum = i
    for j in str(i):
        sum += int(j)
    arr[sum] = False

for k in range(1, n+1):
    if arr[k]:
        print(k)
