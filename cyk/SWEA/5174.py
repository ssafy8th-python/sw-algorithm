import sys
sys.stdin = open("sample_input.txt", "r")
T = int(input())

def find(n):
    global cnt
    visited[n] = True
    tmp = []
    for i in range(len(tree)):
        if tree[i] == n:
            if not visited[i]:
                find(i)
                cnt += 1
    return cnt
for tc in range(1, 1+T):
    node, n = map(int, input().split())
    lst = list(map(int, input().split()))
    tree = [0] * (max(lst)+1)       # [0, 4, 0, 5, 6, 6, 2]

    for i in range(0, len(lst), 2):
        tree[lst[i+1]] = lst[i]
    cnt = 0
    visited = [False] * (max(lst)+1)
    print(f'#{tc} {find(n)+1}')
