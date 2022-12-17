n = int(input())

arr = list(map(int, input().split()))

sum_lst = [arr[0]]

for i in range(1, n):
    sum_lst.append(max(sum_lst[i-1] + arr[i], arr[i]))

print(max(sum_lst))
