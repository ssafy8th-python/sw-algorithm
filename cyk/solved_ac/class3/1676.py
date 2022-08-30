# 팩토리얼 0의 개수
n = int(input())
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

lst = list(map(int, str(factorial(n))))
cnt = 0
for elem in lst[::-1]:
    if elem == 0:
        cnt += 1
    else :
        print(cnt)
        break