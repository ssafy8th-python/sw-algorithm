n = 9
lst = [int(input()) for _ in range(n)]

def check(lst):
    total = sum(lst)
    for i in range(n-1):
        for j in range(i + 1, n):
            if total - lst[i] - lst[j] == 100:
                lst.pop(j)
                lst.pop(i)
                return lst

for i in sorted(check(lst)):
    print(i)