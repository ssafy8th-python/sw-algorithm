t = int(input())

for j in range(t):
    num_lst = list(map(int,input().split()))
    result = 0

    for i in num_lst:
        if i % 2:
            result += i
    
    print(f'#{j + 1} {result}')