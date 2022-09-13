T = int(input())


for test_case in range(1, T+1):
    N, M, L = map(int, input().split())     # 노드의 수, 리프 노드의 수, 출력할 노드

    nodes = [0] * (N + 1)

    for _ in range(M):
        v, w = map(int, input().split())
        nodes[v] = w

    for i in range(N, 1, -1):
        nodes[i//2] += nodes[i]

    print(f'#{test_case} {nodes[L]}')
