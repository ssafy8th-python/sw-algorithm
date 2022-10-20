import sys
input = sys.stdin.readline


def search_parent(node):
    while node != vertex[node]:
        node = vertex[node]
    return node


n, m = map(int, input().split())

vertex = [i for i in range(n)]

result = 0
cnt = 0
for _ in range(m):
    v1, v2 = map(int, input().split())
    p1 = search_parent(v1)
    p2 = search_parent(v2)
    cnt += 1

    if p1 == p2 and not result:
        result = cnt
        break
    else:
        vertex[p2] = p1

print(result)