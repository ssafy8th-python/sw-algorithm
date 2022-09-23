arr = [1, 2, 3, 4]
n = len(arr)

for i in range(0, (1 << n)):
    for j in range(0, n):
        if i & (1 << j):
            print(f'{arr[j]}', end=" ")
    print()