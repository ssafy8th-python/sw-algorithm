n = int(input())

mod = 1000000

p = mod // 10 * 15

fibo = [0] * p

fibo[0] = 0
fibo[1] = 1

for idx in range(2, p):
    fibo[idx] = (fibo[idx-1] + fibo[idx-2]) % mod

print(fibo[n % p])
