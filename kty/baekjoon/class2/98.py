import sys
input = sys.stdin.readline
K, M = map(int, input().split())
lan = [int(input()) for _ in range(K)]
div = sum(lan)//M #231
lst = list(range(1,div+1))
middle = div//2 # 115
start = 0
end = div
maxV = 0
while start <= end:
    total = 0
    middle = (start+end)//2
    for elem in lan:
        total += (elem // lst[middle])
    if total == M:
        if middle > maxV:
            maxV = middle
        start += 1
    elif total > M:
        start = middle + 1
    else:
        end = middle - 1
print(maxV+1)