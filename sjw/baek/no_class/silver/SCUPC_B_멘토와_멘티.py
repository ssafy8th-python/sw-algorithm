# SCUPC B번 - 멘토와 멘티
# 주소: https://www.acmicpc.net/contest/problem/912/2

# 제출한 답
import sys
input = sys.stdin.readline

N = int(input())
pairs = [list(input().split()) for _ in range(N)]
pairs = sorted(pairs, key=lambda x: x[1], reverse=True)
pairs = sorted(pairs, key=lambda x: x[0])

for pair in pairs:
    print(*pair)