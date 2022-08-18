from itertools import permutations

N, M = map(int, input().split())

lst = list(map(int, input().split()))

result = set(permutations(lst, M))
result = list(result)
result.sort()

for res in result:
    for num in res:
        print(num, end=' ')
    print()
