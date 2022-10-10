def nCr(N, r, start):
    if r == 0:
        print(result)
        return
    
    for i in range(start, N - r + 1):
        result[r-1] = arr[i]
        nCr(N, r - 1, i + 1)

N = 5
r = 3

arr = [1, 2, 3, 4, 5]
result = [0] * r

nCr(N, r, 0)

