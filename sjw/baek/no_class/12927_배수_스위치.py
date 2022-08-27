# 12927 배수 스위치
# 주소: https://www.acmicpc.net/problem/12927

# 제출한 답
import sys
input = sys.stdin.readline


def check():
    if 'Y' not in bulbs:
        return 0
    cnt = 0
    for i in range(1, n):
        if bulbs[i] == 'Y':
            cnt += 1
            for j in range(i, n, i):
                if bulbs[j] == 'Y':
                    bulbs[j] = 'N'
                else:
                    bulbs[j] = 'Y'
            if 'Y' not in bulbs:
                return cnt
    return -1


bulbs = ['N'] + list(input().rstrip())
n = len(bulbs)
print(check())
