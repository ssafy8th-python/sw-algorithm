# n개 중 n개를 선택하는 순열  nPn
# 값이 들어가 있는 상황에서의 순열

def f(lst, r):
    if r == N:
        print(lst)
    else:
        for i in range(r, N):
            lst[r], lst[i] = lst[i], lst[r]
            f(lst, r+1)
            lst[r], lst[i] = lst[i], lst[r]


lst = [1, 2, 3]

N = len(lst)

f(lst, 0)
