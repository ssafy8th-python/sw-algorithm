# 색종이 만들기
# 첫째 줄에는 하얀색 종이의 개수, 두째 줄에는 파란색 종이의 개수 출력
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
blue, white = 0, 0
def divide(x,y,n):
    global blue, white
    tmp = 0
    for i in range(x,x+n):
        for j in range(y,y+n):
            tmp += arr[i][j]
    if tmp == 0:
        white += 1
    elif tmp == n*n:
        blue += 1
    else:
        divide(x, y, n//2)
        divide(x+n//2, y, n//2)
        divide(x, y+n//2, n//2)
        divide(x+ n//2, y+n//2, n//2)

divide(0,0,n)
print(white)
print(blue)
