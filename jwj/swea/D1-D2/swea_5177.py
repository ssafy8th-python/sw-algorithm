T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    result = 0
    heapq = [int(1e9)]

    arr_num = 0
    for num in arr:
        heapq.append(num)
        arr_num += 1

        cal_num = arr_num
        while cal_num > 1:
            if heapq[cal_num] < heapq[cal_num//2]:
                heapq[cal_num], heapq[cal_num//2] = heapq[cal_num//2], heapq[cal_num]
            else:
                break
            cal_num //= 2

    while arr_num > 1:
        result += heapq[arr_num//2]
        arr_num //= 2

    print(f'#{test_case} {result}')
