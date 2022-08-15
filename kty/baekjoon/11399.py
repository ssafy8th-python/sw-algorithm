T = int(input())
time = list(map(int, input().split()))

time.sort()
total = 0
sum = 0
for i in range(T):
    sum += time[i]
    total += sum
print(total)