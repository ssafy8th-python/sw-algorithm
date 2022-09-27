def partition(left, right):
    pivot = A[left]
    i, j = left, right

    while i <= j:
        # pivot 보다 큰 값이 나올 때까지 이동
        while i <= j and A[i] <= pivot:
            i += 1

        # pivot 보다 작은은 값이 나올 때까지 동
        while i <= j and A[j] >= pivot:
            j -= 1

        if i < j:
            A[i], A[j] = A[j], A[i]

    A[left], A[j] = A[j], A[left]

    return j


def qsort(left, right):
    if left < right:
        s = partition(left, right)
        qsort(left, s-1)
        qsort(s+1, right)


A = [7, 2, 5, 3, 4, 5]
N = len(A)
qsort(0, N-1)

print(A)
