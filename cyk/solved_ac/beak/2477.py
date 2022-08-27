# 참외밭
K = int(input())
lst = []
pos = []
mx_h, mx_w, mn_h, mn_w = 0, 0, 0, 0
for i in range(6):
    ipt = list(map(int, input().split()))
    lst.append(ipt)
    if ipt[0] == 1 or ipt[0] == 2:
        if mx_w < ipt[1]:
            mx_w = ipt[1]

    elif ipt[0] == 3 or ipt[0] == 4:
        if mx_h < ipt[1]:
            mx_h = ipt[1]
for i in range(6):
    if lst[i % 6][0] == lst[(i+2)%6][0] and lst[(i+1) % 6][0] == lst[(i+3)%6][0]:
        print((mx_h * mx_w - (lst[(i+1)%6][1] * lst[(i+2)%6][1]))*K )
        break

