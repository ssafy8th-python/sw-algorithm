# 종이자르기

W, H = map(int, input().split())
n = int(input())
ipt_dct = {0: [], 1: []}
ipt_dct[0].append(0)
ipt_dct[1].append(0)

ipt_dct[0].append(H)
ipt_dct[1].append(W)

for _ in range(n):
    pos, cut = map(int, input().split())
    ipt_dct[pos].append(cut)
mx_H, mx_W = 0, 0
H_lst = sorted(ipt_dct.get(0))
W_lst = sorted(ipt_dct.get(1))

for i in range(len(H_lst)-1):
    if H_lst[i+1] - H_lst[i] > mx_H:
        mx_H = H_lst[i+1] - H_lst[i]
for i in range(len(W_lst)-1):
    if W_lst[i+1] - W_lst[i] > mx_W:
        mx_W = W_lst[i+1] - W_lst[i]
print(mx_H*mx_W)