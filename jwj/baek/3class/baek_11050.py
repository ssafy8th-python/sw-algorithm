def factorial(f) :
    if f == 0 :
        return 1
    return f * factorial(f-1)

n, k = map(int, input().split())

print(int(factorial(n)/(factorial(n-k)*factorial(k))))