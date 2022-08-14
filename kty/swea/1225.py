import sys

sys.stdin = open("input_1225.txt", "r")

def password(num):
    while True:
        for i in range(1, 6):
            new = num[0] - i
            if new <= 0:
                new = 0
                num.append(new)
                del num[0]
                return num
            num.append(new)
            del num[0]

T = 10
for _ in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    result = password(arr)
    print(f'#{N}',end =' ')
    print(*result)