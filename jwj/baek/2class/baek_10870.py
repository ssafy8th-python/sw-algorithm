
n = int(input())

a = b = 1

if n == 0:
    print(0)
elif n == 1:
    print(1)
else:
    for _ in range(n-2):
        temp = a + b
        a = b
        b = temp

    print(b)

