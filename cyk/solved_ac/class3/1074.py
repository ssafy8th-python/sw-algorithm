# Z
N, r, c = map(int, input().split())
def z(row, col, n):
    global cnt
    if n == 2:
        for i in range(0, n):
            for j in range(0, n):
                if row+i == r and col+j == c:
                    print(cnt)
                    exit(0)
                cnt +=1

        return

    if row <= r < row+n//2 and col <= c < col +n//2: # 좌상
        z(row, col, n//2)
    else:
        cnt += (n//2)**2

    if row <= r < row+n//2 and col+n//2 <= c < col +n: # 우상
        z(row, col + n // 2, n // 2)

    else:
        cnt += (n//2)**2

    if row + n // 2 <= r < row + n and col <= c < col + n // 2:  # 좌하
        z(row+n//2, col, n//2)

    else:
        cnt += (n//2)** 2

    if row+n//2 <= r < row+n and col +n//2<= c < col +n: # 우하
        z(row+n//2, col+n//2, n//2)
    else:
        cnt += (n//2)**2
cnt = 0
z(0,0,2**N)