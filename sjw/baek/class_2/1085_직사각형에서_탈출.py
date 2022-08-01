# 1085 직사각형에서 탈출
# 주소: https://www.acmicpc.net/problem/1085

# 제출한 답
# x, y, w, h = map(int, input().split())

# garo = x - w
# sero = y - h

# if x <= abs(garo) and x <= abs(sero) and x <= y:
#     print(x)
# elif y <= abs(garo) and y <= abs(sero) and y <= x:
#     print(y)
# elif abs(garo) <= abs(sero) and abs(garo) <= x and abs(garo) <= y:
#     print(abs(garo))

# else:
#     print(abs(sero))

# 다른 답
# x,y,w,h = map(int,input().split() )
# print(min(w-x,h-y,x,y))               # min을 왜 까먹는 걸까?