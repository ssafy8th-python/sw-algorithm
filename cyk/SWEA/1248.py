# 공통조상
import sys
sys.stdin = open("input.txt", "r")
T = int(input())

def find(X):
    res = []
    while True:
        for idx, lst in enumerate(arr):
            if X in lst:
                X = idx
                res.append(X)
        if X == 1:
            break
    return res

def tree(com):
    q = [com]
    cnt = 1
    while q:
        x = q.pop(0)
        cnt += len(arr[x])
        for elem in arr[x]:
            q.append(elem)

    return cnt
for tc in range(1, 1+T):
    V, E, X, Y = map(int, input().split()) # 정점의 개수, 간선의 개수, 공통 조상을 찾는 두 개의 정점 번호
    ipt = list(map(int, input().split()))
    arr = [[] for _ in range(V+1)]
    for i in range(0,len(ipt), 2):
        arr[ipt[i]].append(ipt[i+1])
    tmp = len(set(find(X)) &set(find(Y)))
    com = find(X)[::-1][tmp-1]


    print(f'#{tc} {com} {tree(com)}')