# 1654 랜선 자르기
# 주소: https://www.acmicpc.net/problem/1654

# 제출한 답
import sys
input = sys.stdin.readline


def parametric(n, arr):                      # 매개 변수 탐색으로 풀이
    start = 1                                # 확실한 것 중 가장 큰 값
    end = arr[-1]                            # 적당히 큰 값
    while start <= end:
        mid = (start + end) // 2
        cnt = 0
        for i in arr:
            cnt += i // mid
        if cnt >= n:
            start = mid + 1
        else:
            end = mid - 1

    return end


K, N = map(int, input().split())

k_lst = [int(input()) for _ in range(K)]
k_lst.sort()


print(parametric(N, k_lst))
