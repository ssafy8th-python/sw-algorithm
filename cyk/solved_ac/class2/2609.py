a, b = map(int, input().split())
n = min(a,b)

while True :
    if a % n == 0 and b % n == 0 :
        result = n
        break
    n = n - 1

print(result, result*(a//result)*(b//result))