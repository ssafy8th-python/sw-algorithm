# 직사각형
'''
3 10 50 60 100 100 200 300
45 50 600 600 400 450 500 543
11 120 120 230 50 40 60 440
35 56 67 90 67 80 500 600
'''
for _ in range(4):
    x1,y1,p1,q1,x2,y2,p2,q2 = list(map(int, input().split()))
    if p1 < x2  or p2 < x1 or q1 < y2 or y1 > q2:
        print('d')
        continue
    elif x1 == p2 or p1 == x2:
        if y1 == q2 or y2 == q1:
            print('c')
            continue
        else:
            print('b')
            continue
    elif y2 == q1 or q2 == y1:
        print('b')
        continue
    else:
        print('a')