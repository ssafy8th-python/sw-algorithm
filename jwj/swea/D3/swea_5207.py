T = int(input())


def binary_search(num, start, end):

    left = right = True

    while start <= end:
        mid = (start + end) // 2

        if num == n_arr[mid]:
            return 1

        if num < n_arr[mid]:
            end = mid - 1
            if right:
                left = True    # 오른쪽에서 시작합니다.
                right = False
            else:
                return 0
        else:
            start = mid + 1
            if left:
                left = False
                right = True
            else:
                return 0
    return 0


for test_case in range(1, T+1):
    N, M = map(int, input().split())

    n_arr = sorted(list(map(int, input().split())))
    m_arr = list(map(int, input().split()))

    result = 0

    for i in m_arr:
        result += binary_search(i, 0, N-1)

    print(f'#{test_case} {result}')
