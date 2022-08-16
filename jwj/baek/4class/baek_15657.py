from itertools import combinations_with_replacement

N, M = map(int, input().split())

lst = list(map(int, input().split()))
lst.sort()

for strs in list(combinations_with_replacement(lst, M)):
    for char in strs:
        print(char, end=' ')
    print()


