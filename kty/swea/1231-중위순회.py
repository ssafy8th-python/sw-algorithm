import sys

sys.stdin = open("input_1231.txt", "r")



def pre(root):
    if root:
        pre(tree[int(root)][1])
        print(tree[int(root)][0], end = '')
        pre(tree[int(root)][2])

T = 10
for tc in range(1, T + 1):
    v = int(input())
    lst = [list(input().split()) for _ in range(v)]
    tree = [[0, 0, 0] for _ in range(v + 1)]

    '''
    #1 초기에 tree를 만들어 놓은 경우          [[0, 0, 0], ...]
    for i in range(1, len(a)):
        tree[int(a[0])] = a[i]
    
    #2 [[] for _ ] 의 형태로 만들어 놓은 경우  [[], []..]
    for i in range(1, len(a)):
        tree[int(a[0])].append(a[0])
        
    #3 #2나 일차원 배열로 만들어 놓은 경우     []
    tree[int(a[0])] = a[1:len(a)]
    '''
    for i in range(len(lst)):
        p = lst[i][0]
        a = lst[i][1]
        tree[int(p)][0] = a
        if len(lst[i]) == 3:
            c1 = lst[i][2]
            tree[int(p)][1] = c1
        elif len(lst[i]) == 4:
            c1 = lst[i][2]
            c2 = lst[i][3]
            tree[int(p)][1] = c1
            tree[int(p)][2] = c2
    print(f'#{tc}', end = ' ')
    pre(1)
    print()
