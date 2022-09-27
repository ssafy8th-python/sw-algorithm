# 퀵정렬
# 퀵 정렬을 구현해 N개의 정수를 정렬해 리스트 A에 넣고, A[N//2]에 저장된 값을 출력하는 프로그램을 만드시오.

'''
2
5
2 2 1 1 3
10
7 5 4 1 2 10 3 6 9 8
'''
T = int(input())

def partitionH(L, R):
    p = L
    i = L+1
    j = R
    while i <= j:
        while i <= j and lst[i] <= lst[p]:
            i += 1
        while i <= j and lst[j] > lst[p]:
            j -= 1
        if i < j:
            lst[i], lst[j] = lst[j], lst[i]
    lst[p], lst[j] = lst[j], lst[p]
    return j

def q_sort(L, R):
    if L < R:
        p = partitionH(L, R)
        q_sort(L, p-1)
        q_sort(p+1, R)



for tc in range(1, 1+T):
    N = int(input())
    lst = list(map(int, input().split()))
    q_sort(0, len(lst)-1)
    print(f'#{tc} {lst[N//2]}')