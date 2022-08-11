n, m = map(int, input().split())

n_lst = [0] * 101
n_lst[0] = 1
n_lst[1] = 1
n_lst[2] = 2

for i in range(3, 101):
    n_lst[i] = n_lst[i-1] * i

result = n_lst[n] // (n_lst[(n - m)] * n_lst[m])

print(result)


