# 1676 팩토리얼 0의 개수
# 주소: https://www.acmicpc.net/problem/1676

# 제출한 답
def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n - 1)


N = int(input())
cnt = 0
for i in str(factorial(N))[::-1]:
    if i == '0':
        cnt += 1
    else:
        break

print(cnt)