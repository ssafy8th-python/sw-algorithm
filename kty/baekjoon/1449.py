N, L = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
end = arr[0] + L
tape = 1
for i in range(1, N):
    if arr[i] < end:
        continue
    else:
        tape += 1
        end = arr[i] + L

print(tape)