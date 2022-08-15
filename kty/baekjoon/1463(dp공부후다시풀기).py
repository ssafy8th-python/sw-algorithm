n = int(input())
cnt = 0
while n > 1:
    if n % 3 == 0:
        n //= 3
    elif n % 3 == 1:
        n -= 1
        n //= 3
        cnt += 1
    elif n % 2 == 0:
        n //= 2
    cnt += 1
print(cnt)