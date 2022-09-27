T = int(input())


def partition(left, right):
    i, j = left, right

    pivot = arr[left]

    while i <= j:
        while i <= j and arr[i] <= pivot:
            i += 1

        while i <= j and arr[j] >= pivot:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[left], arr[j] = arr[j], arr[left]

    return j


def qsort(left, right):

    if left >= right:
        return

    s = partition(left, right)
    qsort(left, s-1)
    qsort(s+1, right)


for test_case in range(1, T+1):
    N = int(input())

    arr = list(map(int, input().split()))

    qsort(0, N-1)

    print(f'#{test_case} {arr[N//2]}')
