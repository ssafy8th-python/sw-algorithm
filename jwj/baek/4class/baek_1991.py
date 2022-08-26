def pre_order(root):

    if root != -19:
        s = chr(root+65)
        s += pre_order(tree[root][0])
        s += pre_order(tree[root][1])

        return s

    return ''


def in_order(root):

    if root != -19:
        s = in_order(tree[root][0])
        s += chr(root+65)
        s += in_order(tree[root][1])

        return s

    return ''


def post_order(root):

    if root != -19:
        s = post_order(tree[root][0])
        s += post_order(tree[root][1])
        s += chr(root + 65)

        return s

    return ''


N = int(input())

tree = [[] for _ in range(N)]

for _ in range(N):
    nodes = list(input().split())

    tree[ord(nodes[0])-65].append(ord(nodes[1])-65)
    tree[ord(nodes[0])-65].append(ord(nodes[2])-65)


print(pre_order(0))
print(in_order(0))
print(post_order(0))
