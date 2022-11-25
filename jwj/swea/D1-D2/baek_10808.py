s = input()

arr = [0] * (122-96)

for c in s:
    arr[ord(c) - 97] += 1

print(*arr)