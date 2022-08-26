# 빙고
'''
11 12 2 24 10
16 1 13 3 25
6 20 5 21 17
19 4 8 14 9
22 15 7 23 18
5 10 7 16 2
4 22 8 17 13
3 18 1 6 25
12 19 23 14 21
11 24 9 20 15
'''

def bingo(arr): # 빙고 판별 함수
    bingo =0
    for lst in arr:
        if sum(lst) == 0:
            bingo += 1
        if bingo == 3:
            return True

    vert_arr = list(zip(*arr))
    for lst in vert_arr:
        if sum(lst) == 0:
            bingo += 1
        if bingo == 3:
            return True

    x_sum = 0
    x_sum_left = 0
    for i in range(5):
        x_sum += arr[i][i]
        x_sum_left += arr[4-i][i]
    if x_sum == 0:
        bingo += 1
        if bingo == 3:
            return True

    if x_sum_left == 0:
        bingo += 1
        if bingo == 3:
            return True
    return False

bingo_arr = [list(map(int, input().split())) for _ in range(5)]     # 빙고판
check = [list(map(int, input().split())) for _ in range(5)]         # 빙고 체크
count = 0
bingo_count = 0
isbreak = False
for i in range(5):
    for j in range(5):
        checking = check[i][j]
        count += 1
        for k in range(5):
            for t in range(5):
                if bingo_arr[k][t] == checking:
                    bingo_arr[k][t] = 0
        if bingo(bingo_arr):
            print(count)
            isbreak = True
            break
    if isbreak:
        break