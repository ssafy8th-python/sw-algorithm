
N = int(input())

arr = []
rope = [0] * 10001
tmp = [0] * N

for _ in range(N):
    num = int(input())
    arr.append(num)
    rope[num] += 1

for idx in range(1, 10001):
    rope[idx] += rope[idx-1]

maxV = rope[0]

for num in arr:
    tmp[rope[num]-1] = num
    rope[num] -= 1

for idx in range(N):
    sumV = tmp[idx] * (N - idx)

    if maxV < sumV:
        maxV = sumV

print(maxV)