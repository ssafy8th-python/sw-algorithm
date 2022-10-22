import sys
input = sys.stdin.readline


N, M = map(int, input().split())

memory_lst = list(map(int, input().split()))
charge_lst = list(map(int, input().split()))
result = sum(charge_lst)

weight = result
array = [[0] * (result + 1) for _ in range(N + 1)]

# 메모리
for i in range(1, N+1):
    # 비용
    for j in range(1, weight+1):

        if j < charge_lst[i-1]:
            array[i][j] = array[i-1][j]
        else:
            array[i][j] = max(array[i-1][j], array[i-1][j-charge_lst[i-1]] + memory_lst[i-1])

        if array[i][j] >= M:
            result = min(result, j)

print(result)