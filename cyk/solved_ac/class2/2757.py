T = int(input())

while T > 0 :
    k = int(input())
    n = int(input())
    floor = list(range(1,n+1))
    # print(floor)
    up_floor=[]
    for _ in range(0, k):
        for i in range(0, n):
            up_floor.append(sum(floor[0:i+1]))
        floor = up_floor[-n:]
    print(up_floor[-1])
    T -= 1    

# 재귀 절대 쓰지 말것
# T = int(input())

# while T > 0 :
#     k = int(input())
#     n = int(input())
#     result = []
#     def test(k, n):
#         for i in range(1,n+1):
#             result.append((k-1, i))
#         return result
#     # print(test(k,n))# [(1, 1), (1, 2), (1, 3)]
#     last = []
#     for elem in test(k,n) :
#         if elem[0] == 0:
#             last.append(elem[1])
#         else :
#             test(elem[0], elem[1])
#     print(sum(last))
#     T -= 1    

