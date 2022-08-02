t = int(input())

for j in range(t):
    num_lst = list(map(int,input().split()))
    result = sum(num_lst) / 10
    
    print(f'#{j + 1} {round(result)}')