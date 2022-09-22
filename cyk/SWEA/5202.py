# 화물도크
import sys
sys.stdin = open("sample_input (7).txt", "r")
'''
1
5
20 23
17 20
23 24
4 14
8 18
'''
T = int(input())
for tc in range(1, 1+T):
    n = int(input())
    arr = [list(map(int, list(input().split()))) for _ in range(n)]
    arr.sort(key=lambda x:x[1])
    cnt = 0
    lst = [arr[0]]
    for i in range(1, n):
        if lst[-1][1] <= arr[i][0]:
            lst.append(arr[i])
    print(f'#{tc} {len(lst)}')