# 2xn 타일링
lst = [1,2]
n = int(input())
for i in range(2, n):
    lst.append(lst[i-2]+lst[i-1])
print(lst[n-1]%10007)