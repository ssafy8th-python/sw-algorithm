def factorial(f) :
    if f == 1 :
        return 1
    return f * factorial(f-1)

n, k = map(int, input().split())
if k == 0 or n == k:
    print(1)
else :
    print(int(factorial(n)/(factorial(n-k)*factorial(k))))
