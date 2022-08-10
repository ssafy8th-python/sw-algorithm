N = int(input())
num = 0
for i in range(0, len(str(N))):
    a = str(N)[i]
    num += int(a)

print(num)