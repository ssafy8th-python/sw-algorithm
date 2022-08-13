primes = [False, False] + [True] * 1000000
A = 1
B = 1000000
for num in range(2, B+1):
    if primes[num]:
        for idx in range(num+num, B+1, num):
            primes[idx] = False
 
TC = int(input())
for tc in range(1, TC+1):
    D, A, B = map(int, input().split())
    cnt = 0
    for idx in range(A, B+1):
        if primes[idx] and str(D) in str(idx):
            cnt += 1
    print(f'#{tc} {cnt}')
