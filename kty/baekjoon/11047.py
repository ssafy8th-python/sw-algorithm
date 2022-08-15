n, money = map(int, input().split())
coin = [int(input()) for _ in range(n)]
coin.sort(reverse=True)

cnt = 0
for i in coin:
    n = money // i
    cnt += n
    money = money % i

print(cnt)