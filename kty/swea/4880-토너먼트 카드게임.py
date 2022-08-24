
# 숫자 1은 가위 2는 바위 3은 보

import sys
sys.stdin = open("input_4880.txt", "r")

def divide(st, ed):
    if st == ed: # 한 명만 있으면 리턴
        return st
    left = divide(st, (st + ed) // 2)
    right = divide((st+ed) // 2 + 1, ed)
    return winner(left, right)

def winner(a, b):
    if cards[a] == cards[b]: # 비긴 경우
        return a
    elif cards[a] - cards[b] == 1 or cards[a] - cards[b] == -2: # a가 이길 경우
        return a
    return b

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    cards = list(map(int, input().split()))
    print(f'#{tc} {divide(0, n-1)+1}')




