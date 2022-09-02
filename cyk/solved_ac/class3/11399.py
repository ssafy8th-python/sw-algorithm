# ATM
n = int(input())
s = sorted(list(map(int, input().split())))
sumV = 0
for i in range(n):
    sumV += s[i]*(n-i)
print(sumV)