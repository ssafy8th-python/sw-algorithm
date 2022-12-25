N, Q = map(int, input().split())
song = []
for i in range(1, N+1):
    b = int(input())

    for _ in range(b):
        song.append(i)

for _ in range(Q):
    index = int(input())

    print(song[index])