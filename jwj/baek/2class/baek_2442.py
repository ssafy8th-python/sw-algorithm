N = int(input())

for i in range(N):
    for space in range(1, N - i):
        print(' ', end="")
    for star in range(i*2 + 1):
        print('*', end="")
    print()