# 숫자만들기
# 최대와 최소가 되는 수식을 찾고 그 두 값의 차이를 출력
import sys
sys.stdin = open("sample_input (4).txt", "r")

def calc(k, state):
    global mx, mn
    if k == N:
        if state > mx:
            mx = state
        if state < mn:
            mn = state
        return

    for i in range(4):
        if op_inp[i]:
            op_inp[i] -= 1

            if i == 0:
                calc(k+1, state+num[k])
            elif i == 1:
                calc(k+1, state-num[k])
            elif i == 2:
                calc(k+1, state*num[k])
            elif i == 3:
                calc(k+1, state//num[k] if state > 0 else -(abs(state)//num[k]))
            op_inp[i] += 1

T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    op_inp = list(map(int, input().split()))
    num = list(map(int, input().split()))
    mx, mn = -10e9, 10e9
    calc(1,num[0])
    print(f'#{tc} {mx-mn}')
