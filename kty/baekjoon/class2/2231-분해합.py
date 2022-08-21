N = int(input())

for i in range(N):
    zari = sum(map(int, str(i)))
    result = i + zari
    if result == N:
        print(i)
        break
else:
    print(0)
