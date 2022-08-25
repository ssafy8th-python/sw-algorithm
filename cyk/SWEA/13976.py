# 기지국
'''
1
9
XXXXXXXXX
XXCHXBXXX
XXHAHXXHX
XXHHXXXXX
XXXXXXXXX
XXAHHXXXX
XXHXXHAHX
XXAHXXHXX
XXHXHXXCX
XXXXXXXXX
'''

T = int(input())
for tc in range(1, 1+T):
    n = int(input())
    arr = [list(input()) for _ in range(n+1)]
    home = 0
    cover = 0
    for lst in arr:
        home += lst.count('H')
    K = 0
    for row in range(n):
        for col in range(n):
            if arr[row][col] == 'A':
                K = 1
            if arr[row][col] == 'B':
                K = 2
            if arr[row][col] == 'C':
                K = 3

            for k in range(1, K + 1):
                for dr, dc in [[0,1], [1,0], [0,-1], [-1,0]]:
                    if 0 <= row+dr*k < n and 0 <= col+dc*k < n and arr[row+dr*k][col+dc*k] == 'H':
                        cover += 1
                        arr[row + dr * k][col + dc * k] = 'X'

            K = 0

    print(f'#{tc} {home - cover}')