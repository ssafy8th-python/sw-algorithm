# 요리사
import sys
sys.stdin = open("sample_input (4).txt", "r")

def calc(lst):
    res = 0
    for i in lst:
        for j in lst:
            if i != j:
                res += arr[i][j]
    return res

def comb(k, s):
    global lst, MIN
    if k == R:

        a_lst = result
        b_lst = [x for x in range(N) if not x in a_lst]
        lst.append(a_lst)
        lst.append(b_lst)
        tmp = abs(calc(a_lst) - calc(b_lst))
        if tmp < MIN:
            MIN = tmp
        return

    for i in range(s, N-(R-k)+1):
        result[k] = i
        comb(k+1, i+1)



T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    R = N//2
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = [-1]*R
    lst = []
    MIN = 100000000
    comb(0,0)
    print(f'#{tc} {MIN}')
