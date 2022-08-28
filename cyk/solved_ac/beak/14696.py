# 딱지놀이
'''
1
1 4
4 3 3 2 1
'''
n = int(input())
for _ in range(n):
    A = [0]*5
    B = [0]*5
    a_lst = list(map(int, input().split()))
    b_lst = list(map(int, input().split()))
    for elem in a_lst[1:]:
        A[elem] += 1
    for elem in b_lst[1:]:
        B[elem] += 1

    if A[4] > B[4]:
        print('A')
    elif A[4] == B[4]:
        if A[3] > B[3]:
            print('A')
        elif A[3] == B[3]:
            if A[2] > B[2]:
                print('A')
            elif A[2] == B[2]:
                if A[1] > B[1]:
                    print('A')
                elif A[1] == B[1]:
                    print('D')
                else:
                    print('B')
            else:
                print('B')
        else:
            print('B')
    else:
        print('B')