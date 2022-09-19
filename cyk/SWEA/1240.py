# 단순 2진 암호코드
# 숫자 하나는 7개의 비트로 암호화되어 주어진다.
#
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, 1+T):
    N, M = map(int, input().split())
    code = []
    arr = [list(map(int, list(input()))) for _ in range(N)]
    for lst in arr:
        if sum(lst) != 0:
            f_lst = lst[::-1]
            start = f_lst.index(1)
            code = f_lst[start:start+56]
            break
    f_code = code[::-1]
    tmp = []
    for i in range(0, 56, 7):
        if f_code[i:i+7] == [0, 0, 0, 1, 1, 0, 1]:
            tmp.append(0)
        elif f_code[i:i + 7] == [0, 0, 1, 1, 0, 0, 1]:
            tmp.append(1)
        elif f_code[i:i + 7] == [0, 0, 1, 0, 0, 1, 1]:
            tmp.append(2)
        elif f_code[i:i + 7] == [0, 1, 1, 1, 1, 0, 1]:
            tmp.append(3)
        elif f_code[i:i + 7] == [0, 1, 0, 0, 0, 1, 1]:
            tmp.append(4)
        elif f_code[i:i + 7] == [0, 1, 1, 0, 0, 0, 1]:
            tmp.append(5)
        elif f_code[i:i + 7] == [0, 1, 0, 1, 1, 1, 1]:
            tmp.append(6)
        elif f_code[i:i + 7] == [0, 1, 1, 1, 0, 1, 1]:
            tmp.append(7)
        elif f_code[i:i + 7] == [0, 1, 1, 0, 1, 1, 1]:
            tmp.append(8)
        elif f_code[i:i + 7] == [0, 0, 0, 1, 0, 1, 1]:
            tmp.append(9)
    res = 0
    for i in range(0,8):
        if i % 2:   # 홀수자리
            res += tmp[i]
        else:
            res += tmp[i]*3
    print(f'#{tc} ', end='')
    if res % 10:
        print(0)
    else:
        print(sum(tmp))
