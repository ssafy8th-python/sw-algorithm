from math import ceil

N = int(input())

rooms = list(map(int, input().split()))

master, sub = map(int, input().split())

result = N

for room in rooms:
    room -= master
    if room > 0:
        result += ceil(room / sub)

print(result)