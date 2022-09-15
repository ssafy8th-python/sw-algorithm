# 파도반 수열
lst = [1, 1, 1]
T = int(input())
ipt = [int(input()) for _ in range(T)]
for i in range(3, 101):
    lst.append(lst[i-3]+lst[i-2])
for elem in ipt:
    print(lst[elem-1])