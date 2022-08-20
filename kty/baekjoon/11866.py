N, K = map(int, input().split())
arr = []
for i in range(1, N+1):
    arr.append(i)

result = []
dead = K-1
while len(arr) != 0:
    while dead >= len(arr):
        dead -= len(arr)
    result.append(arr.pop(dead))
    dead += K-1

print(f'<{", ".join(map(str, result))}>')