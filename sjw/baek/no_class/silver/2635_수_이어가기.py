# 2635 수 이어가기
# 주소: https://www.acmicpc.net/problem/2635

# 제출한 답
# import sys
# input = sys.stdin.readline

n = int(input())

maxcnt = 0
maxlst = []
for i in range(1, n + 1):
    a = n  # 앞의 앞에 수
    b = i  # 앞의 수
    c = 0  # 현재수
    cnt = 1
    tmp = [n, b]
    while c >= 0:
        c = a - b
        tmp.append(c)
        a = b
        b = c
        cnt += 1
    if maxcnt < cnt:
        maxcnt = cnt
        maxlst = tmp

maxlst.pop()
print(maxcnt)
print(*maxlst)
