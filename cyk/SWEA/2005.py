 # 파스칼의 삼각형
# N = int(input())
# ARR = [[] for _ in range(N+1)]
# for row in range(1, N+1):
#     for col in range(row+1):
#         if col == 0 or col == N-1:
#             ARR[row].append(1)
#         else:
#             ARR[row].append(ARR[row-1][col-1] + ARR[row-1][col])
#         print(row, col)
#
# print(ARR)

T = int(input())

for tc in range(1, 1+T):
    n = int(input())
    arr = [[] for _ in range(n)]
    for row in range(n):
        for col in range(row+1):
            if col == 0 or col == row:
                arr[row].append(1)
            else:
                arr[row].append(arr[row-1][col-1] + arr[row-1][col])
    print(f'#{tc}')
    for lst in arr:
        print(*lst)
