# 트리
# 트리가 주어졌을 때 노드를 지우면 남은 트리에서 리프 노드의 개수를 구하는 프로그램 작성

# 첫째 줄에 트리의 노드의 개수 N이 주어진다. N은 50보다 작거나 같은 자연수이다.
# 둘째 줄에는 0번 노드부터 N-1번 노드까지, 각 노드의 부모가 주어진다.
# 만약 부모가 없다면 (루트) -1이 주어진다. 셋째 줄에는 지울 노드의 번호가 주어진다.

def dfs(v):
    global r_lst
    visited[v] = True
    r_lst.append(v)
    for i in range(N):
        if not visited[i]:
            if tree[i] == v:
                dfs(i)

N = int(input())
ipt = list(map(int, input().split()))
rNode = int(input())
tree = [0]*N
r_lst = []
for i in range(N):
    tree[i] = ipt[i]
# print(tree) [-1, 0, 0, 2, 2, 4, 4, 6, 6]

visited = [False]*N
dfs(rNode)
cnt = 0
for elem in r_lst:
    tree[elem] = -2
result = [-1]
for i in range(0, N):
    if not i in r_lst:
        if not i in tree:
            cnt +=1
print(cnt)

# [-1, 0, 0, -2, -2, -2, -2, -2, -2]
# [-1, 0, -2, 1, 1]
