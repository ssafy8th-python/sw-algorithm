T = int(input())
while T > 0 :
    H, W, N = list(map(int, input().split()))
    if N%H == 0:
        result = (H*100) + (N//H)
    else :
        result = (N%H)*100 + (N//H) +1
    print(result)
    T=T-1