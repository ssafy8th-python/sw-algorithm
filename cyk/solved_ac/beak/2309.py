# 일곱 난쟁이
'''
20
7
23
19
10
15
25
8
13
'''

lst = []
for _ in range(9):
    ipt = int(input())
    lst.append(ipt)
sumV = sum(lst)
check = False
idx1, idx2 = 0, 0
for elem1 in lst:
    for elem2 in lst:
        temp = sumV - elem1 - elem2
        if temp == 100 and elem1 != elem2:
            check = True
            break
    if check:
        break
res = []

for i in range(9):
    if lst[i] == elem1:
       continue

    elif lst[i] == elem2:
       continue

    res.append(lst[i])
for elem in sorted(res):
    print(elem)