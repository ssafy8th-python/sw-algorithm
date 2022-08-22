n = int(input())
k = 1
cnt = 1
while n > k:
    k += 6 * cnt
    cnt += 1
print(cnt)