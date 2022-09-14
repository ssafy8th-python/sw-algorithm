# # 1, 2, 3 더하기
T = int(input())
ipt = []
for _ in range(T):
    ipt.append(int(input()))

lst = [1, 2, 4]
for i in range(3, 12):
    lst.append(lst[i-1]+lst[i-2]+lst[i-3])
for elem in ipt:
    print(lst[elem-1])
