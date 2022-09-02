# 9375 패션왕 신해빈
# 주소: https://www.acmicpc.net/problem/9375

# 제출한 답

t = int(input())

for _ in range(t):
    c = dict()
    n = int(input())
    for _ in range(n):
        a, b = input().split()
        if b in c:
            c[b] += 1
        else:
            c[b] = 1
    result = 0
    tmp = 1

    for i in list(c.values()):
        result += i
        tmp *= i
    if len(c) == 1:
        print(result)
    else:
        print(result + tmp)

