# 부분합
# 연속된 수들의 부분합 중에 그 합이 S 이상이 되는 것 중 가장 짧은 것의 길이 구하기
# 합을 만드는 것이 불가능하다면 -1 출력
import sys
input = sys.stdin.readline
N, S = map(int, input().split())
lst = list(map(int, input().split()))
mn = N
start = end = 0
sumV = lst[0]

if sum(lst) < S:
    print(0)
elif sum(lst) == S:
    print(N)
else:
    while True:
        if sumV < S:
            end += 1
            if end >= N:
                break
            sumV += lst[end]
        else:
            cnt = end - start + 1
            if start >= N:
                break
            sumV -= lst[start]
            start += 1
            if cnt < mn:
                mn = cnt
    print(mn)

