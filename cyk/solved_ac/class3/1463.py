# 1로만들기

def makeOne(n):
    one = [0, 0]
    for i in range(2, n+1):
        temp = []
        if i % 2 == 0:
            temp.append(one[i//2]+1)
        if i % 3 == 0:
            temp.append(one[i//3]+1)
        temp.append(one[i-1]+1)
        one.append(min(temp))
    return one[-1]
n = int(input())
print(makeOne(n))