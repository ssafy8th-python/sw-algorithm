import sys
input = sys.stdin.readline

def search(start, end, idx):

    while start <= end:
        mid = (start + end) // 2

        if N_lst[mid] == M_lst[idx]:
            return True

        elif N_lst[mid] < M_lst[idx]:
            start = mid + 1

        elif N_lst[mid] > M_lst[idx]:
            end = mid - 1

    return False


N = int(input())
N_lst = list(map(int, input().split()))

M = int(input())
M_lst = list(map(int, input().split()))

N_lst.sort()

for idx in range(M):
    if search(0, N-1, idx):
        print(1)
    else:
        print(0)

