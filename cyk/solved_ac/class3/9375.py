# 패션왕 신해빈
'''
2
3
hat headgear
sunglasses eyewear
turban headgear
3
mask face
sunglasses face
makeup face
'''
# from itertools import combinations        메모리초과

T = int(input())
for tc in range(T):
    n = int(input())
    dct = dict()
    for _ in range(n):
        val, cate = input().split()
        if not(cate in dct.keys()):
            dct[cate] = 1
        else:
            dct[cate] = dct.get(cate) + 1

    lst = list(dct.values())
    result = 1
    for elem in lst:
        result *= (elem+1)
    print(result-1)