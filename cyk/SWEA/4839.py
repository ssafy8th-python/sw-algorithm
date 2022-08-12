# import sys
# sys.stdin = open("4839.txt", "r")

def binarySearch(N, key):
    start = 1
    end = N
    cnt = 0
    while start <= end:
        cnt += 1
        middle = (start + end) // 2
        if middle == key:
            return cnt
        elif middle > key:
            end = middle
        else:
            start = middle
    return 0


T = int(input())

for tc in range(1, T+1):
    N, A, B = map(int, input().split())


    result_a = binarySearch( N, A)
    result_b = binarySearch( N, B)

    # print(result_a, result_b)

    if result_a < result_b:
        print(f'#{tc} A')
    elif result_a > result_b:
        print(f'#{tc} B')
    elif result_a == result_b:
        print(f'#{tc}', 0)

