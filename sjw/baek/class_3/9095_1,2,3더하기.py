# 9095 1,2,3 더하기
# 주소: https://www.acmicpc.net/problem/9095

# 제출한 답
def check(k):
    if lst[k] != 0:
        return lst[k]
    else:
        lst[k] = check(k - 1) + check(k - 2) + check(k - 3)
        return lst[k]


t = int(input())

lst = [0, 1, 2, 4] + [0] * 8

for _ in range(t):
    n = int(input())

    print(check(n))
