# 1629 곱셈
# 주소: https://www.acmicpc.net/problem/1629

# 제출한 답
import sys
# input = sys.stdin.readline

a, b, c = map(int, input().split())


def Dac(a, b):
    if b == 1:
        return a % c
    temp = Dac(a, b // 2)

    if b % 2:
        return temp * temp * a % c
    else:
        return temp * temp % c


print(Dac(a, b))