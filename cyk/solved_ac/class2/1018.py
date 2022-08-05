n, k = map(int, input().split())
result =[]
for _ in range(n):
    a = list(input())
    result.append(a)
print(n,k,result)

for lst in result :
    count = 0
    for x in range(0,k-8+1):
        for y in range(0,n-8+1):
            if lst[x][y] == 'B' :
                for idx, i in enumerate(lst):  
                    if idx % 2 :
                        if i == 'B':
                            count += 1
                    else :
                        if i == 'W':
                            count += 1
            else :
                for idx, i in enumerate(lst):  
                    if idx % 2 :
                        if i == 'W':
                            count += 1
                    else :
                        if i == 'B':
                            count += 1    
        
    print(count)            




    
