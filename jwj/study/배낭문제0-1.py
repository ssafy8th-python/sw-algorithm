
# # 재귀
# def knapsack(capacity, n):
#
#     # 가방이 가득차거나 모든 물건을 검색한 경우
#     if capacity == 0 or n == 0:
#         return 0
#
#     # 다음에 넣을 물건의 부피가 용량보다 큰 경우
#     if size[n-1] > capacity:
#         return knapsack(capacity, n-1)
#     else:
#         return max(value[n-1] + knapsack(capacity-size[n-1], n-1), knapsack(capacity, n-1))
#
#
# size = [30, 10, 20, 35, 40]
# value = [3, 0, 3, 5, 4]
# print(knapsack(60, 5))


# 반복문

def knapsack1(capacity, n):
    array = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # 물건을 하나 씩 넣음
    for i in range(1, n+1):
        # 배낭이 무개
        for s in range(1, capacity + 1):
            if size[i-1] > s:       # 물건의 부피가 s보다 크면
                array[i][s] = array[i - 1][s]   # 이전 물건 그대로 가지고 있음
            else:                   # 물건의 부피가 s보다 작거나 같으면
                array[i][s] = max(array[i-1][s], value[i - 1] + array[i-1][s-size[i-1]])

            print(f'{array[i][s]}', end=' ')
        print()
    return array[n][capacity]


size = [9, 3, 4, 7, 8]
value = [13, 4, 5, 10, 11]
print(knapsack1(10, 5))
