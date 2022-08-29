# 색종이
'''
2
0 0 10 10
2 2 6 6
'''

arr = [[0]*1002 for _ in range(1002)]
n = int(input())
for num in range(1, n+1):
    x, y, s1, s2 = map(int, input().split())
    for i in range(y, y+s2):
        for j in range(x, x+s1):
            arr[i][j] = num

result=[]
for num in range(1, n+1):
    res = 0
    for i in range(1002):
        for j in range(1002):
            if arr[i][j] == num:
                res += 1
    result.append(res)
for i in result:
    print(i)