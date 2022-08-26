# 14696 딱지놀이
# 주소: https://www.acmicpc.net/problem/14696

# 제출한 답
import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    Alst = [0] * 5
    Blst = [0] * 5
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    for i in a[1:]:
        Alst[i] += 1
    for j in b[1:]:
        Blst[j] += 1

    for i in range(4, 0, -1):
        if Alst[i] > Blst[i]:
            print('A')
            break
        elif Alst[i] < Blst[i]:
            print('B')
            break
    else:
        print('D')
