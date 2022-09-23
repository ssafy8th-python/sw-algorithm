# 정훈이의 높은 선반
import sys
sys.stdin = open("input (12).txt","r")

def subset(lst):
    for i in range(0, 1<<n):        # 부분집합의 개수
        tmp = 0
        for j in range(0,n):        # 원소의 수만큼 비트를 비교
            if i & (1<<j):          # i의 j번째 비트가 1이면 j번째 원소 출력
                tmp += lst[j]
        if tmp >= B:
            res.append(tmp)

T = int(input())
for tc in range(1, 1+T):
    n, B = map(int, input().split())
    lst = list(map(int, input().split()))
    res = []
    subset(lst)
    res.sort()
    print(f'#{tc} {res[0]-B}')
