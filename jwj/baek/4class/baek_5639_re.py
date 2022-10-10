import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

def dfs(start, end):
    if start > end:
        return

    end_temp = end + 1

    for i in range(start+1, end+1):
        if arr[start] < arr[i]:
            end_temp = i
            break
    
    dfs(start + 1, end_temp-1)
    dfs(end_temp, end)
    
    print(arr[start])

arr = []
while True:
    try:
        arr.append(int(input()))
    except:
        break

dfs(0, len(arr) - 1)