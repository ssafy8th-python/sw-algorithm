lst = [0] * 31

for _ in range(28):
    n = int(input())
    lst[n] = 1

for i in range(1, 31):
    if lst[i] == 0:
        print(i)