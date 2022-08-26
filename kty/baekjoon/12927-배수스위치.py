

def sw(arr):
    cnt = 0
    for i in range(len(arr)):
        if arr.count('N') == len(arr):
            break
        if arr[i] == 'Y':
            cnt += 1
            for j in range(i, len(arr), i+1):
                if arr[j] == 'Y':
                    arr[j] = 'N'
                else:
                    arr[j] = 'Y'
    else:
        return -1
    return cnt

arr = list(input())
print(sw(arr))