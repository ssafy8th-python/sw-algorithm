N = int(input())
lst = list(range(1,N+1))
count = 0

while len(lst) > 1:
    if count % 2:
        a = lst.pop(0)
        lst.append(a)
        count += 1
    else:
        lst.pop(0)
        count += 1
print(lst[0])