import sys
sys.stdin = open("input.txt", "r")

def operation(lst, n):
    tree = [0]*(n+1)
    idx = n
    for i in range(n,0,-1):
        if len(lst[i]) == 1:
            tree[i] = int(lst[i][0])
        else:
            if lst[i][0] == '+':
                tree[i] = tree[int(lst[i][1])] + tree[int(lst[i][2])]
            elif lst[i][0] == '-':
                tree[i] = tree[int(lst[i][1])] - tree[int(lst[i][2])]
            elif lst[i][0] == '/':
                tree[i] = tree[int(lst[i][1])] // tree[int(lst[i][2])]
            elif lst[i][0] == '*':
                tree[i] = tree[int(lst[i][1])] * tree[int(lst[i][2])]
    return tree

for tc in range(1, 11):
    n = int(input())
    lst = [[] for _ in range(n+1)]
    for _ in range(n):
        ipt = input().split()
        for elem in ipt[1:]:
            lst[int(ipt[0])].append(elem)
    print(f'#{tc} {operation(lst, n)[1]}')