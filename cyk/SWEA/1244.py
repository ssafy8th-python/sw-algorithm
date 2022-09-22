# 최대상금
# 최대 여섯자리수, 최대 10번의 교환횟수
'''
1
123 1
'''
def f(k, lst):
    global res

    if k == count:
        tmp = ''
        for elem in lst:
            tmp += f'{elem}'
            if res < int(tmp):
                res = int(tmp)
        return

    for i in range(size):
        for j in range(i+1, size):
            new_lst = lst[::]
            x, y = lst[i], lst[j]
            new_lst[i], new_lst[j] = y, x
            f(k+1, new_lst)

T = int(input())
for tc in range(1, 1+T):
    num_lst, count = input().split()
    num_lst, count= list(map(int, list(num_lst))), int(count)
    size = len(num_lst)
    res = 0
    f(0, num_lst)
    print(f'#{tc} {res}')