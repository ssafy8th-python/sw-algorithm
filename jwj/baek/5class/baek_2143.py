def two_pointer(lst, number):
    lp = 0
    rp = 1
    n_len = len(lst)
    sum_value = lst[0]
    res = 0

    while True:
        if sum_value < number:
            if rp == n_len:
                break
            sum_value += lst[rp]
            rp += 1
        elif sum_value > number:
            if lp == n_len:
                break
            sum_value -= lst[lp]
            lp += 1
        else:
            if lp == n_len:
                break
            sum_value -= lst[lp]
            lp += 1
            res += 1

    return res


T = int(input())

n = int(input())

A = list(map(int, input().split()))

m = int(input())

B = list(map(int, input().split()))

dp1 = [-1] * 1000001
dp2 = [-1] * 1000001

result = 0

for i in A:
    if dp1[i] == -1:
        tmp = two_pointer(B, T - i)
        result += tmp
        dp1[i] = tmp
    else:
        result += dp1[i]

for i in B:
    if dp2[i] == -1:
        tmp = two_pointer(A, T - i)
        result += tmp
        dp2[i] = tmp
    else:
        result += dp2[i]


for i in A:
    tmp = T - i
    for j in B:
        if tmp == j:
            result -= 1

print(result)
