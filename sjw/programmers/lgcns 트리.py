def solution(edges, roots):
    edLen = len(edges)
    answer = [0] * edLen
    for i in roots:
        visited = [0] * edLen
        s = [i]
        while s:
            v = s.pop()
            for j in range(edLen):
                if not visited[j]:
                    if edges[j][0] == v:
                        s.append(edges[j][1])
                        visited[j] = 1
                    elif edges[j][1] == v:
                        s.append(edges[j][0])
                        edges[j][0], edges[j][1] = edges[j][1], edges[j][0]
                        answer[j] += 1
                        visited[j] = 1

    return answer


# 루트가 바뀔 때 부모자식이 역전되는데 각각의 노드는 몇 번 역전되었나
for edge, root in [[[[1, 3], [1, 2], [2, 4], [2, 5]], [2, 3]], [[[1, 2], [1, 3], [2, 4]], [3, 4, 1, 2]]]:
    print(solution(edge, root))
    # [1, 2, 0, 0] / [3, 2, 2]
