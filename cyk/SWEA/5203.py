# 베이비진 게임
import sys
sys.stdin = open("sample_input (7).txt","r")

def f(lst):
    if 3 in lst:    # 3개가 연달아 들어왔을때
        return True
    for i in range(8):
        if lst[i] and lst[i + 1] and lst[i + 2]:    # 연속된 숫자가 3개일때
            return True
    return False

T = int(input())
for tc in range(1, 1+T):
    cards = list(map(int, input().split()))

    counts1 = [0] * 10
    counts2 = [0] * 10
    flag = True

    print(f'#{tc}', end=' ')

    for elem in cards:
        if flag:
            counts1[elem] += 1
            flag = False
            if f(counts1):
                print(1)
                break
        else:
            counts2[elem] += 1
            flag = True
            if f(counts2):
                print(2)
                break
    else:
        print(0)

