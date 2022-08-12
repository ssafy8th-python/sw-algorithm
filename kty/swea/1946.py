T = int(input())

for t in range(T) :
    N = int(input())
    value = ""
    for i in range(N) :
        C, K = input().split()
        value += C * int(K)

    print("#{}".format(t+1))
    for i in range(len(value)) :
        if (i+1)%10 == 0 :
            print(value[i])
        else :
            print(value[i], end="")
    print()