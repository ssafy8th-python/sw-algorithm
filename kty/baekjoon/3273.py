n = int(input())
arr = list(map(int, input().split()))
x = int(input())

cnt = 0
arr.sort()
st = 0
ed = len(arr)-1
while st != ed:
    if arr[st] + arr[ed] == x:
        st += 1
        cnt += 1
    elif arr[st] + arr[ed] > x:
        ed -= 1
    else:
        st += 1

print(cnt)
