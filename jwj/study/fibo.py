# def fibo(n):
#     if n < 2:
#         return n
#     else:
#         return fibo(n-1) + fibo(n-2)
#
#
# for i in range(21):
#     print(i, fibo(i))
#

def fibo(n):
    if memo[n] == -1:
        memo[n] = fibo(n-1) + fibo(n-2)

    return memo[n]


memo = [-1] * 201
memo[0] = 0
memo[1] = 1

for i in range(101):
    print(i, fibo(i))
