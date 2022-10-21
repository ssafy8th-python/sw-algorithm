# 리모컨
# 1. 100에서 원하는 수까지 +, - 하는 경우
# 2. 리모컨으로 숫자를 누르는 경우

import sys
input = sys.stdin.readline


N = int(input())
M = int(input())
if M == 0:
    wrong =[]
else:
    wrong = list(map(int, input().split()))
btn = [x for x in range(0,10) if x not in wrong]

res1 = abs(100 - int(N))
res2 = 0

n1, n2 = N, N
cnt1, cnt2 = 0,0
while True:
    for elem in list(str(n1)):
        if int(elem) not in btn:
            break
    else:
        break
    if cnt1 >= res1:
        break
    n1 += 1
    cnt1 += 1



while True:
    if n2 < 0:
        cnt2 = 1e9
        break

    for elem in list(str(n2)):
        if int(elem) not in btn:
            break
    else:
        break

    if cnt2 >= res1:
        break
    n2 -= 1
    cnt2 += 1

cnt1+=len(list(str(n1)))
cnt2+=len(list(str(n2)))
print(min(cnt1,cnt2, res1))
