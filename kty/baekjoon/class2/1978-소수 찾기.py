N = int(input())
nums = list(map(int, input().split()))

# 에라토스테네스의 체
sosu = [False] + [False] + [True] * 1000
for i in range(2, round(1000**0.5)+1):
    if sosu[i]:
        for j in range(i*2, 1001, i):
            sosu[j] = False

cnt = 0
for num in nums:
    if sosu[num]:
        cnt += 1

print(cnt)