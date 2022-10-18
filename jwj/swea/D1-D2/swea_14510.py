T = int(input())

for test_case in range(1, T+1):
    N = int(input())

    trees = list(map(int, input().split()))

    remain_tree = 0

    max_tree = max(trees)

    tmp_tree = []
    s = 0

    for tree in trees:
        if tree != max_tree:
            n_v = max_tree - tree
            tmp_tree.append(n_v)
            s += n_v

    day = 1

    while 0 < s:
        if day % 2:
            s -= 1
            for idx, num in enumerate(tmp_tree):
                if num == 1:
                    tmp_tree.pop(idx)
                    break
            else:
                for idx, num in enumerate(tmp_tree):
                    if num > 2:
                        tmp_tree[idx] -= 1
                        break
                else:
                    s += 1
        else:
            s -= 2
            for idx, num in enumerate(tmp_tree):
                if num == 2:
                    tmp_tree.pop(idx)
                    break
            else:
                for idx, num in enumerate(tmp_tree):
                    if num > 2:
                        tmp_tree[idx] -= 2
                        break
                else:
                    s += 2

        day += 1
    print(f'#{test_case} {day-1}')