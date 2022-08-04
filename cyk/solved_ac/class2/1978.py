n = int(input())
result = []
x = list(map(int, input().split()))
for i in x:
    count = 0

    for j in range(1,i+1):
        if i % j == 0 :
            count+=1
    if count == 2 :    
        result.append(i)

print(len(result))