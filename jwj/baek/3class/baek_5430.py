for test_case in range(int(input())):
    p = input()
    p = list(p)
    n = int(input())
    x = input().strip('[]')
    if x:
        x = list(map(int, x.split(',')))
    
    left = True
    error = False
    for char in p:
        if char =='R':
            left = not left
        else :
            if not x:
                error = True
                break 
            if left:
                x.pop(0)
            else :
                x.pop(-1)
    if error :
        print('error')
    elif not x :
        print('[]')
    else :
        if left : 
            print('[',end='')
            for num in x[:-1]:
                print(f'{num},', end='')
            print(x[-1], end='')
            print(']')
        else : 
            x.reverse()
            print('[',end='')
            for num in x[:-1]:
                print(f'{num},', end='')
            print(x[-1], end='')
            print(']')


    