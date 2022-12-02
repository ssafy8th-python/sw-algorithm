# 11725 트리의 부모 찾기
# 주소: https://www.acmicpc.net/problem/11725

# 제출한 답
# import sys
# input = sys.stdin.readline

start = 0
for i in [3,1,4]:
    start = start ^ i
    print(start)