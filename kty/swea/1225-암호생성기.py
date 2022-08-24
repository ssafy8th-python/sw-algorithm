import sys

sys.stdin = open("input_1225.txt", "r")

def password(num):
    while True:
        for i in range(1, 6):
            new = num.pop(0) - i
            if new <= 0:
                new = 0
                num.append(new)
                return num
            num.append(new)

T = 10
for _ in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    result = password(arr)
    print(f'#{N}',end =' ')
    print(*result)