t = int(input())

for j in range(t):
    num_lst = list(map(int,input().split()))
    
    print(f'#{j + 1} {max(num_lst)}')