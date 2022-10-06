A, B = map(int, input().split())
C = int(input())

hour = (A + ((B+C) // 60)) % 24
minute = (B+C) % 60

print(hour, minute)

