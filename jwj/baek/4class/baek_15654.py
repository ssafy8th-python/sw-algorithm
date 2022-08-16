from itertools import permutations

N, M = map(int, input().split())

lst = list(map(int, input().split()))
lst.sort()

for strs in list(permutations(lst, M)):
    for char in strs:
        print(char, end=' ')
    print()


