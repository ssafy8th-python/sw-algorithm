S = int(input())
i = 1
cnt = 0

while S >= 0:
    cnt += 1
    S -= i
    i += 1

print(cnt-1)
