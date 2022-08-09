N = int(input())

lst = list(range(1,N+1))



while len(lst)>1 :
    lst[2:].append(lst[1])
    
print(lst[0])
