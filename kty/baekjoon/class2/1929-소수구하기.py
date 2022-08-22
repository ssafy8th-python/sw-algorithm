n, m = map(int, input().split())
K = 1000000
sosu_lst = [False] + [False] + [True] * K
for num in range(2, round(K**0.5)+1):
    if sosu_lst[num]:
        for j in range(num*2, K, num):
            sosu_lst[j] = False

for idx in range(n, m + 1):
    if sosu_lst[idx]:
        print(idx)