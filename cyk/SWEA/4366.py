# 정식이의 은행 업무
import sys
sys.stdin = open("sample_input (3).txt", "r")

def solution(n):
    result = ''
    while n:
        result += str(n%3)
        n = n//3
    return result[::-1]
T = int(input())
for tc in range(1,1+T):
    b_lst = list(input())
    t_lst = list(input())
    b_n, t_n = len(b_lst), len(t_lst)
    res = []
    for i in range(b_n):
        if b_lst[i] == '0':
            b_lst[i] = '1'
        else:
            b_lst[i] = '0'
        res.append(int(''.join(b_lst),2))
        if b_lst[i] == '0':
            b_lst[i] = '1'
        else:
            b_lst[i] = '0'
    for elem in res:
        if len(solution(elem)) == t_n:
            cnt = 0
            for i in range(t_n):
                if solution(elem)[i] != t_lst[i]:
                    cnt += 1
            if cnt == 1:
                print(f'#{tc} {elem}')
                break
