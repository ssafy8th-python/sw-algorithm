# 경비원
# 동근이의 위치와 각 상점 사이의 최단 거리의 합
'''
10 5
3
1 4
3 2
2 8
2 3
'''
# 북: 1, 남: 2, 서: 3, 동: 4
# 북쪽 남쪽에 위치한 경우 블록의 왼쪽경계로부터의 거리
# 동쪽 서쪽에 위치한 경우 블록의 위쪽 경계로부터의 거리
col, row = map(int, input().split())
n = int(input())
stores = [list(map(int, input().split())) for _ in range(n)]    #상점의 위치
pos, location = map(int, input().split())    # 위치
res = 0

for store in stores:
    if pos == store[0]:             # 같은 줄에 있을 때
        res += abs(location - store[1])
    elif (pos + store[0])%4 == 3:   # 맞은 편 상에 있을 때
        if pos == 1 or pos == 2:    # 북쪽, 남쪽에 위치할 때
            temp1 = row + location + store[1]
            temp2 = row + abs(col - location) + abs(col-store[1])
            if temp1 < temp2:
                res += temp1
            else:
                res += temp2

        else:                       # 동쪽, 서쪽에 위치할 때
            temp1 = col + location + store[1]
            temp2 = col + abs(row - location) + abs(row - store[1])
            if temp1 < temp2:
                res += temp1
            else:
                res += temp2

    else:                           # 기준점에서 측면에 있을 때
        if pos == 1:    # 북쪽일때
            if store[0] == 4:   # 동쪽
                res += (row-location + store[1])
            elif store[0] == 3:
                res += location + store[1]
        elif pos == 2:    # 남쪽일때
            if store[0] == 4:
                res += (col-location+row-store[1])
            else:
                res += (location + row-store[1])
        elif pos == 3:
            if store[0] == 1:
                res += location + store[1]
            else:
                res += row -location + col - store[1]
        else:
            if store[0] ==1:
                res += location + col - store[1]
            else:
                res += row - location + col - store[1]

print(res)