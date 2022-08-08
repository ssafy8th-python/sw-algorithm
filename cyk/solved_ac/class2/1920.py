import sys
input = sys.stdin.readline


N = int(input())
a = (map(int, input().split()))

dict_a = {x : 1 for x in a}

M = int(input())
m = (map(int, input().split()))


for k in m :
    if dict_a.get(k) == 1 :
        print(1)
    else :
        print(0)

