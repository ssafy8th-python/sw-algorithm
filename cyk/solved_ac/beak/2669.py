# 직사각형 네개의 합집합의 면적 구하기
'''
1 2 4 4
2 3 5 7
3 1 6 5
7 3 8 6
'''
lst = [[0]*101 for _ in range(101)]
sumV = 0
for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            if lst[i][j] == 0:
                lst[i][j] += 1
                sumV += 1
            else:
                continue
print(sumV)