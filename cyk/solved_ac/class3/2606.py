# 바이러스
'''
7
6
1 2
2 3
1 5
5 2
5 6
4 7
'''

Com_N = int(input())
pair = int(input())
lst = [[] for _ in range(Com_N+1)]

# def dfs(v):
#     stack = [v]
#     visited[v] = True
#     cnt = 0
#     while stack:
#         v = stack.pop()
#         # print(v)
#
#         for w in lst[v]:
#             if not visited[w]:
#                 stack.append(w)
#                 visited[w] = True
#                 cnt += 1
#     else:
#         return cnt

def dfs(v):
    global cnt
    visited[v] = True
    for w in lst[v]:
        if not visited[w]:
            cnt += 1
            dfs(w)

for _ in range(pair):
    prt, chld = map(int, input().split())
    lst[prt].append(chld)
    lst[chld].append(prt)

visited = [False] * (Com_N+1)
cnt =0
dfs(1)

print(cnt)