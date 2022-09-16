T = int(input())


def post(start):
    global parent
    global cnt

    cnt += 1
    res = 0

    if tree[start]:
        res += post(tree[start][0])

        if len(tree[start]) == 2:
            res += post(tree[start][1])

        if start == c1 or start == c2:
            return res + 1
    else:
        if start == c1 or start == c2:
            return res + 1

    if res == 2:
        parent = start
        res += 1

    return res


for test_case in range(1, T+1):
    V, E, c1, c2 = map(int, input().split())

    tree = [[] for _ in range(V + 1)]

    arr = list(map(int, input().split()))

    for idx in range(E):
        tree[arr[idx * 2]].append(arr[idx * 2 + 1])

    cnt = 0
    parent = 1
    post(1)

    cnt = 0
    post(parent)

    print(f'#{test_case} {parent} {cnt}')
