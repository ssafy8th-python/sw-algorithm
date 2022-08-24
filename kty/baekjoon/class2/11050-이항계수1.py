n, k = map(int, input().split())

def fact(n):
    if n < 2:
        return 1
    else:
        return n * fact(n-1)

print(round(fact(n) / (fact(k) * fact(n-k))))