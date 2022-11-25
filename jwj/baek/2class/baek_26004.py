N = int(input())

arr = [0] * 5

S = input()

for s in S:
    if s == 'H':
        arr[0] += 1
    elif s == 'I':
        arr[1] += 1
    elif s == 'A':
        arr[2] += 1
    elif s == 'R':
        arr[3] += 1
    elif s == 'C':
        arr[4] += 1

print(min(arr))
