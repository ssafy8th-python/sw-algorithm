
def pre_order(root):
    if root != 0:
        pre_order(lst[root][0])
        result.append(lst[root][2])
        pre_order(lst[root][1])


for tc in range(1, 11):
    N = int(input())

    lst = [[0, 0, ''] for _ in range(N+1)]

    for _ in range(N):
        input_lst = list(input().split())

        node, char = int(input_lst[0]), input_lst[1]

        lst[node][2] = char

        if len(input_lst) == 3:
            lst[node][0] = int(input_lst[2])

        elif len(input_lst) == 4:
            lst[node][0] = int(input_lst[2])
            lst[node][1] = int(input_lst[3])

    result = []

    pre_order(1)

    print(f'#{tc}', ''.join(result))
