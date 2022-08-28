# 방배정
'''
16 2
1 1
0 1
1 1
0 2
1 2
0 2
0 3
1 3
1 4
1 3
1 3
0 6
1 5
0 5
1 5
1 6

'''
import math
n, K = map(int, input().split())
girl_lst = [0] * 7
boy_lst = [0] * 7
for _ in range(n):
    g, lev = map(int, input().split())
    if g == 0: # 여학생인 경우
        girl_lst[lev] += 1
    else:
        boy_lst[lev] += 1
room = 0

for elem in girl_lst:
    if 0 < elem <= K:
        room += 1
    elif elem > K:
        room += math.ceil(elem/K)
for elem in boy_lst:
    if 0 < elem <= K:
        room += 1
    elif elem > K:
        room += math.ceil(elem/K)
print(room)