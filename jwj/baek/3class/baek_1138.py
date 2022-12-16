
N = int(input())

lst = list(map(int, input().split()))

arr = [0 for _ in range(N)]

# 키
for i in range(N):
    cnt = 0

    for j in range(N):
        if arr[j] == 0 and lst[i] == cnt:
            arr[j] = i + 1
            break
        elif arr[j] == 0:
            cnt += 1

print(*arr)

