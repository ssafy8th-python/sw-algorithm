N = int(input())

for i in range(N):
    for space in range(i):
        print(' ', end="")

    for star in range((N-i-1)*2 + 1):
        print('*', end="")
    print()