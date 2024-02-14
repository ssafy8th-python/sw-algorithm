# SCUPC A번 - 빅데이터? 정보보호!
# 주소: https://www.acmicpc.net/contest/problem/912/1

# 제출한 답
import sys
input = sys.stdin.readline

N = int(input())
memo = input().strip()
memoLen = len(memo)

check = memoLen - N * 7
half = N // 2
if N == 1:
    if memoLen == 7:
        print('bigdata?')
    else:
        print('security!')
else:
    if check > half:
        print('security!')
    elif check == half:
        print('bigdata? security!')
    else:
        print('bigdata?')