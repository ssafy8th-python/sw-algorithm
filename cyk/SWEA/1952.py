# 수영장
import sys
sys.stdin = open("sample_input (4).txt","r")

def rec(k, state):
    global res
    if k >= 12:
        if res > state:
            res = state
        return
    rec(k+1,state +min(fee[0]*month[k],fee[1]))
    rec(k+3,state +fee[2])


T = int(input())
for tc in range(1, 1+T):
    fee = list(map(int, input().split()))   # 1일, 1달, 3달, 1년
    month = list(map(int, input().split()))
    res = fee[3]
    rec(0, 0)
    print(f'#{tc} {res}')

