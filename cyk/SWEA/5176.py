# 이진 탐색 트리
import sys
sys.stdin = open("sample_input.txt", "r")
def inorder(start):
    global num
    if tree[start]:
        inorder(tree[start][0])
        res[start] = num
        num+=1
        if len(tree[start])==2:
            inorder(tree[start][1])
    else:
        res[start] = num
        num += 1
T = int(input())
for tc in range(1, 1+T):
    node = int(input())
    tree = [[] for _ in range(node+1)]
    for i in range(2, node+1):
        tree[i//2].append(i)
    res = [[] for _ in range(node+1)]
    num = 1
    inorder(1)
    print(f'#{tc} {res[1]} {res[node//2]}')