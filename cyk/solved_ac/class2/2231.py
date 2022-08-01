n = int(input())
def generator(n):
    n_sum = 0
    n_original = n
    while n > 0 :
        n_sum += n % 10
        n = n//10
    return n_sum + n_original

def is_generator(n):
    result =[]
    x = len(str(n))
    # print(x)
    if n <= 18 :
        for i in range(n, n+1):
            result.append(generator(i))
            if n in result :
                return print(i)
            
    for i in range(n-x*9, n+1) :
        # print(i)
        result.append(generator(i))
        if n in result:
            return print(i)
        
    return print('0')
    

is_generator(n)

# brute force 알고리즘 