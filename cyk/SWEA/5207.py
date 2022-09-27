# 이진탐색
'''
3
3 3
1 2 3
2 3 4
3 5
1 3 5
2 4 6 8 10
5 5
1 3 5 7 9
1 2 3 4 5
'''
# def partitionL(L, R):
#     p = R
#     i = L - 1
#     j = L
#     for j in range(L, R):
#         if searchL[j] <= searchL[p]:
#             i += 1
#             searchL[i], searchL[j] = searchL[j], searchL[i]
#     i += 1
#     searchL[p], searchL[i] = searchL[i], searchL[p]
#     return i
#
# def q_sort(L, R):
#     if L < R:
#         p = partitionL(L, R)
#         q_sort(L, p-1)
#         q_sort(p+1, R)


def binary(start, end, key):
    middle = (start+end)//2
    times = []
    while start <= end:
        middle = (start + end) // 2

        if searchL[middle] == key:
            return times
        elif searchL[middle] > key:
            end = middle-1
            if times:
                if times[-1] == 1:
                    return -1
            times.append(1)
        else:
            start = middle+1
            if times:
                if times[-1] == 2:
                    return -1
            times.append(2)
    return -1

T = int(input())
for tc in range(1, 1+T):
    N, M = map(int, input().split())
    searchL = list(map(int, input().split()))
    keyL = list(map(int, input().split()))
    searchL.sort()
    # print(searchL)
    cnt = 0
    for key in keyL:
        result = binary(0, N-1, key)
        if result == -1:
            continue
        cnt += 1
    print(f'#{tc} {cnt}')
