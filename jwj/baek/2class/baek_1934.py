T = int(input())

for _ in range(T):
    a, b = map(int, input().split())
    x, y = a, b
    if a < b:
        a, b = b, a

    while b != 0:
        a = a % b
        a, b = b, a

    print(x * y // a)