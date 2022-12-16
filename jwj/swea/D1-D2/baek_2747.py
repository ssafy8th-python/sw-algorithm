n = int(input())

a = 0
b = 1
c = 0

for _ in range(n-1):
    c = a + b

    a = b
    b = c

if n == 1:
    print(1)
else:
    print(c)