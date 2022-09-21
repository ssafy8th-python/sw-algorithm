# 작업 순서
# 방향성을 가진 간선
import sys
sys.stdin = open("sample_input.txt", "r")
def order(arr):
    while any(arr):
        for idx in range(1, len(arr)):
            if not arr[idx] and not idx in res:  # 비어있다면
                res.append(idx)
                for i in range(1, len(arr)):
                    if idx in arr[i]:
                        find_idx = arr[i].index(idx)
                        arr[i].pop(find_idx)

for tc in range(1, 11):
    V, E = map(int, input().split())
    arr = [[] for _ in range(V + 1)]
    ipt = list(map(int, input().split()))
    start = ipt[0]

    for i in range(0, E * 2, 2):
        arr[ipt[i + 1]].append(ipt[i])
    res = []
    order(arr)
    for i in range(1, len(arr)):
        if not i in res:
            res.append(i)

    print(f'#{tc}', end=' ')
    print(*res)