# 통계학
# 산술평균 : N개의 수들의 합을 N으로 나눈 값
# 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
# 최빈값 : N개의 수들 중 가장 많이 나타나는 값
# 범위 : N개의 수들 중 최댓값과 최솟값의 차이
'''
5
1
3
8
-2
2
'''


import sys
input = sys.stdin.readline

def middle(lst, N):                         # 음수 정렬
    count = 8001
    count_lst = [0] * count
    sumV = 0
    for i in lst:
        count_lst[i] += 1
        sumV += i
    for j in range(-3999, 4001, 1):
        count_lst[j] += count_lst[j-1]
    res = [0] * N
    for k in range(N-1, -1, -1):
        count_lst[lst[k]] -= 1
        res[count_lst[lst[k]]] = lst[k]
    return res, sumV



def counting(lst):                          # 최빈값 구하기
    count_dict = {x: 0 for x in lst}
    for elem in lst:
        count_dict[elem] += 1

    mx = max(count_dict.values())
    count_lst =[]
    for key in count_dict:
        if count_dict.get(key) == mx:
            count_lst.append(key)
    if len(count_lst) > 1:
        return sorted(count_lst)[1]
    return sorted(count_lst)[0]


N = int(input())                             # N은 홀수
lst = [int(input()) for _ in range(N)]
size = len(lst)

sort_lst, sumV = middle(lst, N)
avg = int(round(sumV/size, 0))
print(avg)                                    # 1. 산술 평균
midV = N//2
print(sort_lst[midV])                         # 2. 중앙값
maxV = lst[-1]
print(counting(lst))                          # 3. 최빈값
print(max(lst) - min(lst))                    # 4. 범위
