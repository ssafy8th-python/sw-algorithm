    # def pre_order(T):
#
#     if 비어 있지 않으면:
#         visit(T)
#         pre_order(T.left)
#         pre_order(T.right)
#
#     if 자식 노드가 있으면:
#         visit(T)
#         pre_order(T.left)
#         pre_order(T.right)
#     else:
#         visit(T)

def pre_order(root):
    if root != 0:
        print(root)
        pre_order(tree[root][0])
        pre_order(tree[root][1])


inputS = '1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13'
lst = list(map(int, inputS.split()))
V = 13

tree = [[0, 0] for _ in range(V+1)]
parent = [0] * (V+1)

for idx in range(0, len(lst), 2):
    p, c = lst[idx], lst[idx+1]
    if tree[p][0] == 0:
        tree[p][0] = c
    else:
        tree[p][1] = c

    parent[c] = p

pre_order(1)

print(tree)
print(parent)
