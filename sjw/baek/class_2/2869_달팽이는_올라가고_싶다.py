# 2869 달팽이는 올라가고 싶다
# 주소: https://www.acmicpc.net/problem/2869

# 제출한 답
a, b, v = map(int, input().split())

if v == a:
    print(1)
elif (v - a) % (a - b):
    result = ((v - a) // (a - b)) + 2
    print(result)
else:
    result = ((v - a) // (a - b)) + 1
    print(result)