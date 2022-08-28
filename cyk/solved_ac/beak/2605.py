# 줄세우기
'''
5
0 1 1 3 2
'''
n = int(input())
lst = list(range(1, n+1))               # [1, 2, 3, 4, 5]
line = list(map(int, input().split()))  # [0, 1, 1, 3, 2]
for idx, elem in enumerate(line):
    if idx == 0:
        continue
    else:
        X = lst.pop(idx)
        lst.insert(idx-elem, X)
print(*lst)