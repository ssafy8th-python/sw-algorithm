# 쿼드트리
def qt(row, col, n):   # 시작 row, 시작 col, 변의 길이
    global result

    if n == 1:
        if arr[row][col] ==1:
            # result.append((row, col,1))
            result += '1'
        else:
            # result.append((row, col,0))
            result += '0'

        n *= 2
        return


    tmp = 0
    for r in range(row, row+n):
        for c in range(col, col+n):
            tmp += arr[r][c]
    if tmp == 0:
        # result.append((row, col,0))
        result += '0'

        return
    elif tmp == n*n:
        # result.append((row, col,1))
        result += '1'

        return

    result += '('
    qt(row, col, n//2)

    qt(row, col+n//2, n//2)

    qt(row+n//2, col, n//2)

    qt(row+n//2, col+n//2, n//2)
    result += ')'

n = int(input())
arr = [list(map(int, list(input()))) for _ in range(n)]
result = ''
qt(0,0,n)
for lst in result:
    print(lst,end='')