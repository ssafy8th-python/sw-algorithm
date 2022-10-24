
def is_prime(number):
    for i in range(2, number+1):
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                break
        else:
            prime.append(i)


N = int(input())
prime = []

is_prime(N)

N_len = len(prime)

lp = 0
rp = 1

result = 0

if prime:
    result = prime[0]

answer = 0

while lp != N_len:
    if result < N:
        if rp == N_len:
            break
        result += prime[rp]
        rp += 1
    elif result > N:
        result -= prime[lp]
        lp += 1
    else:
        answer += 1
        result -= prime[lp]
        lp += 1

print(answer)
