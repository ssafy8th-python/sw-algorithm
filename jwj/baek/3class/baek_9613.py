T = int(input())


def gcd(a, b):
    if a < b:
        a, b = b, a

    while b != 0:
        a = a % b
        a, b = b, a

    return a


for _ in range(T):
    lst = list(map(int, input().split()))
    result = 0
    for i in range(1, lst[0]):
        for j in range(i+1, lst[0]+1):
            result += gcd(lst[i], lst[j])

    print(result)
