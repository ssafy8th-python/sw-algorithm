n , m = map(int, input().split())
s = sorted(list(map(int, input().split())), reverse=True)
lst = []
for i in s :
    for j in s :
        if i != j and i + j < m:
            for k in s :
                if k != i and k != j and i+j+k <=m:
                    lst.append(i+k+j)
print(max(lst))


# brute force 알고리즘 : 완전 탐색 알고리즘 가능한 모든 경우의 수를 모두 탐색하면서 요구 조건에 충족되는 결과를 가져온다 -> 순차탐색, 깊이우선탐색(DFS), 너비우선탐색(BFS)