# 중위 순회
'''
8
1 W 2 3
2 F 4 5
3 R 6 7
4 O 8
5 T
6 A
7 E
8 S
'''
import sys
sys.stdin = open("input (5).txt", "r")

def inorder(root):

    if len(tree[root]) == 2:
        inorder(int(tree[root][1]))
        print(tree[root][0],end='')

    elif len(tree[root]) == 3:
        inorder(int(tree[root][1]))
        print(tree[root][0],end='')
        inorder(int(tree[root][2]))
    else:
        print(tree[root][0],end='')

for tc in range(1, 11):
    V = int(input())
    tree = [[] for _ in range(V+1)]         # [[], [], [], [], [], [], [], [], []]
    for _ in range(V):
        lst = input().split()
        tree[int(lst[0])] = lst[1:]
    # print(tree)        # [[], ['W', '2', '3'], ['F', '4', '5'], ['R', '6', '7'], ['O', '8'], ['T'], ['A'], ['E'], ['S']]
    print(f'#{tc} ', end='')
    inorder(1)

    print()
