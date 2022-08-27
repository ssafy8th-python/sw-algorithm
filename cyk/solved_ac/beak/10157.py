# 자리배정
    # 위 오른쪽 아래 왼쪽
dC = [1, 0, -1, 0]
dR = [0, 1, 0, -1]

row, col = map(int, input().split())
K = int(input())
arr = [[0]*col for _ in range(row)]
check = [[False]*col for _ in range(row)]
d = 0
person = 1
cur_row, cur_col = 0,0
while person <= row*col:
    check[cur_row][cur_col] = True
    arr[cur_row][cur_col] = person
    new_R, new_C = cur_row + dR[d], cur_col + dC[d]
    if person == K:
        print(cur_row+1, cur_col+1)
        break
    if new_R < 0 or new_R >= row or new_C < 0 or new_C >= col or check[new_R][new_C] :
        d = (d+1) % 4

    cur_row += dR[d]
    cur_col += dC[d]
    person += 1
else:
    print(0)



# for i in range(1, 1+row):
#     for j in range(1, 1+col):
#         print(i,j)